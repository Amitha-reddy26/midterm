import os
import logging
from abc import ABC, abstractmethod
import pandas as pd

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

class CalculationHistory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename='calculation_history.csv'):
        if not hasattr(self, 'initialized'):
            self.filename = filename
            self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])
            if os.path.exists(self.filename):
                self.history = pd.read_csv(self.filename)
            self.initialized = True

    def add_entry(self, operation, operands, result):
        new_entry = pd.DataFrame({
            'operation': [operation],
            'operands': [operands],
            'result': [result]
        })
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.save_history()

    def save_history(self):
        self.history.to_csv(self.filename, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])
        self.save_history()

    def delete_entry(self, index):
        if 0 <= index < len(self.history):
            self.history = self.history.drop(index).reset_index(drop=True)
            self.save_history()
        else:
            raise IndexError("Invalid index. Cannot delete entry.")

    def show_history(self):
        return self.history


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b


class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b


class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b


class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b


class PowerCommand(Command):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def execute(self):
        return self.base ** self.exponent


class MenuCommand(Command):
    def execute(self):
        return (
            "Available operations: add, subtract, multiply, divide, power, "
            "menu, history, clear, delete"
        )


class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, operation, command):
        self.commands[operation] = command

    def execute_command(self, operation):
        if operation in self.commands:
            return self.commands[operation].execute()
        raise ValueError("Unknown operation.")


class CalculationFacade:
    def __init__(self):
        self.history = CalculationHistory()
        self.handler = CommandHandler()

    def perform_operation(self, operation, a, b):
        command = self.create_command(operation, a, b)
        result = command.execute()
        self.history.add_entry(operation, (a, b), result)
        return result

    def create_command(self, operation, a, b):
        if operation == 'add':
            return AddCommand(a, b)
        if operation == 'subtract':
            return SubtractCommand(a, b)
        if operation == 'multiply':
            return MultiplyCommand(a, b)
        if operation == 'divide':
            return DivideCommand(a, b)
        if operation == 'power':
            return PowerCommand(a, b)
        raise ValueError("Unknown operation.")

    def show_history(self):
        return self.history.show_history()

    def clear_history(self):
        self.history.clear_history()

    def delete_entry(self, index):
        self.history.delete_entry(index)


def main():
    facade = CalculationFacade()
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide, power, menu, history, clear, delete) or 'quit' to exit: ")

        if operation == 'quit':
            logging.info("Exiting the app. Goodbye!")
            break

        if operation == 'menu':
            print("Available operations: add, subtract, multiply, divide, power, menu, history, clear, delete")
            logging.info("Displayed menu options.")
            continue

        if operation == 'history':
            print(facade.show_history())
            logging.info("Displayed calculation history.")
            continue

        if operation == 'clear':
            facade.clear_history()
            print("History cleared.")
            logging.info("Cleared calculation history.")
            continue

        if operation == 'delete':
            index = input("Enter the index of the entry to delete: ")
            try:
                index = int(index)
                facade.delete_entry(index)
                print(f"Entry at index {index} deleted.")
                logging.info(f"Deleted entry at index {index}.")
            except (ValueError, IndexError) as error:
                print(f"Error deleting entry: {error}")
                logging.error("Error deleting entry: %s", error)
            continue

        a = input("Enter first number: ")
        b = input("Enter second number: ")

        try:
            a = int(a)
            b = int(b)
            result = facade.perform_operation(operation, a, b)
            print(f"The result is: {result}")
            logging.info("Executed %s command with result: %s", operation, result)

        except ValueError as error:
            logging.error("Invalid input: %s", error)
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
