import pandas as pd
import os

class CalculationHistory:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename=None):
        if filename and getattr(self, "filename", None) != filename:
            self.filename = filename
            self.history = pd.DataFrame(columns=["operation", "operands", "result"])
            self.redo_stack = []
            directory = os.path.dirname(self.filename)
            if directory:
                os.makedirs(directory, exist_ok=True)
            if os.path.exists(self.filename):
                self.history = pd.read_csv(self.filename)
            return

        if hasattr(self, "initialized"):
            return

        self.filename = filename if filename else "calculation_history.csv"
        directory = os.path.dirname(self.filename)
        if directory:
            os.makedirs(directory, exist_ok=True)

        if os.path.exists(self.filename):
            self.history = pd.read_csv(self.filename)
        else:
            self.history = pd.DataFrame(columns=["operation", "operands", "result"])

        self.redo_stack = []
        self.initialized = True


    def add_entry(self, operation, operands, result):
        operands_str = str(tuple(operands))
        new_entry = pd.DataFrame({
            "operation": [operation],
            "operands": [operands_str],
            "result": [result]
        })
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.redo_stack.clear()
        self.save_history()

    def save_history(self):
        directory = os.path.dirname(self.filename)
        if directory:
            os.makedirs(directory, exist_ok=True)
        self.history.to_csv(self.filename, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "operands", "result"])
        self.redo_stack.clear()
        self.save_history()

    def show_history(self):
        return self.history

    def undo(self):
        if not self.history.empty:
            last_entry = self.history.iloc[-1].to_dict()
            self.redo_stack.append(last_entry)
            self.history = self.history.iloc[:-1].reset_index(drop=True)
            self.save_history()
            return "Undo successful"
        return "Nothing to undo"

    def redo(self):
        if self.redo_stack:
            entry = self.redo_stack.pop()
            df = pd.DataFrame([entry])
            self.history = pd.concat([self.history, df], ignore_index=True)
            self.save_history()
            return "Redo successful"
        return "Nothing to redo"
