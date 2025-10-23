import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        pass  

    def start(self):
        self.load_plugins()
        while True:
            user_input = input("Enter a command (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                raise SystemExit("Exiting app.")
            result = self.command_handler.execute_command(user_input)
            if result is None:
                print(f"No such command: {user_input}")
            else:
                print(result)
