from typing import List
from calculator.calculation import Calculation

class Calculations:
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls._history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return list(cls._history)

    @classmethod
    def clear_history(cls):
        cls._history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        return cls._history[-1] if cls._history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        return [calc for calc in cls._history if calc.operation.__name__ == operation_name]
