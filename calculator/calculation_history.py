import pandas as pd
import os

class CalculationHistory:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename='calculation_history.csv'):
        if not hasattr(self, "initialized"):
            self.filename = filename
            self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])
            self.redo_stack = []  

            if os.path.exists(self.filename):
                self.history = pd.read_csv(self.filename)

            self.initialized = True

    def add_entry(self, operation, operands, result):
        operands_str = str(operands)
        new_entry = pd.DataFrame({
            'operation': [operation],
            'operands': [operands_str],
            'result': [result]
        })
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.redo_stack.clear()  
        self.save_history()

    def save_history(self):
        self.history.to_csv(self.filename, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])
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
            return "Undo successful "
        return "Nothing to undo "

    def redo(self):
        if self.redo_stack:
            entry = self.redo_stack.pop()
            self.history = pd.concat([self.history, pd.DataFrame([entry])], ignore_index=True)
            self.save_history()
            return "Redo successful "
        return "Nothing to redo "
