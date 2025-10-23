import pandas as pd
import os

class CalculationHistory:
    def __init__(self, filename='calculation_history.csv'):
        self.filename = filename
        self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])

        if os.path.exists(self.filename):
            self.history = pd.read_csv(self.filename)

    def add_entry(self, operation, operands, result):
        operands_str = str(operands)  
        new_entry = pd.DataFrame({'operation': [operation], 'operands': [operands_str], 'result': [result]})
        self.history = pd.concat([self.history, new_entry], ignore_index=True)

    def save_history(self):
        self.history.to_csv(self.filename, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'operands', 'result'])

    def show_history(self):
        return self.history
