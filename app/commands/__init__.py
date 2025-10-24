import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from abc import ABC, abstractmethod
from calculator.calculation_history import CalculationHistory

# ✅ Base Command class for static operations
class Command(ABC):
    @abstractmethod
    def execute(self, a=None, b=None):
        pass


class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name):
        command = self.commands.get(name)

        if not command:
            logging.error(f"No such command: {name}")
            return f"No such command: {name}"

        # ✅ If plugin was initialized with values (pytest usage) → execute directly
        if hasattr(command, "a") and hasattr(command, "b") and command.a is not None and command.b is not None:
            return command.execute()

        # ✅ Commands requiring NO input
        simple_cmds = ["undo", "redo", "menu", "history", "clear", "delete", "exit"]
        if name in simple_cmds:
            return command.execute()

        # ✅ Standard interactive mode (CLI)
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = command.execute(a, b)

            # ✅ If successful, save to history
            CalculationHistory().add_entry(name, (a, b), result)
            return result

        except ValueError:
            return "Invalid number input ❌"
        except ZeroDivisionError as e:
            return str(e)
        except Exception as e:
            logging.error(f"Execution error: {e}")
            return f"Error executing command: {e}"


class App:
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        self.configure_logging()
        self.settings = self.load_environment_variables()
        self.command_handler = CommandHandler()

    def configure_logging(self):
        if os.path.exists("logging.conf"):
            logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        load_dotenv()
        settings = dict(os.environ)
        logging.info(f"Environment variables loaded. ENV={settings.get('ENVIRONMENT', 'PRODUCTION')}")
        return settings

    def load_plugins(self):
        plugins_package = "app.plugins"
        plugins_path = plugins_package.replace(".", "/")

        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory missing: {plugins_path}")
            return

        for _, plugin, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    module = importlib.import_module(f"{plugins_package}.{plugin}")
                    self.register_plugin_commands(module, plugin)
                except ImportError as e:
                    logging.error(f"Failed to load plugin '{plugin}': {e}")

    def register_plugin_commands(self, module, plugin_name):
        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name.lower(), item())
                logging.info(f"Command '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        logging.info("Application started. Type 'exit' to quit.")

        while True:
            cmd = input(">>> ").strip().lower()

            if cmd == "exit":
                logging.info("Exiting application...")
                break

            result = self.command_handler.execute_command(cmd)
            print(result)


if __name__ == "__main__":
    App().start()
