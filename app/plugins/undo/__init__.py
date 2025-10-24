from app.commands import Command
from calculator.calculation_history import CalculationHistory

class Undo(Command):
    def execute(self, a=None, b=None):
        history = CalculationHistory()
        return history.undo()
