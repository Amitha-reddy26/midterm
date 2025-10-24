import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, a=None, b=None):
        pass


class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, operation, command):
        self.commands[operation] = command

    def execute_command(self, operation):
        command = self.commands.get(operation)

        if not command:
            error_message = f"No such command: {operation}"
            logging.error(error_message)
            return error_message

        # ✅ Commands that do NOT require number inputs
        non_math_commands = ["undo", "redo", "menu", "history", "clear", "delete", "exit"]

        if operation in non_math_commands:
            return command.execute()

        # ✅ Math commands require numbers
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = command.execute(a, b)

            # ✅ Save results to history for Undo/Redo support
            from calculator.calculation_history import CalculationHistory
            history = CalculationHistory()
            history.add_entry(operation, (a, b), result)

            return result

        except ValueError:
            return "Invalid number input ❌"
        except Exception as e:
            logging.error(f"Execution error: {e}")
            return f"Error executing command: {e}"


class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return

        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)

            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == "exit":
                    logging.info("Exiting application...")
                    sys.exit(0)

                result = self.command_handler.execute_command(cmd_input)
                print(result)

        except KeyboardInterrupt:
            logging.info("Application interrupted. Exiting…")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")


if __name__ == "__main__":
    app = App()
    app.start()
