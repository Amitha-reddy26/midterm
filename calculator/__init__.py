
from decimal import Decimal
from typing import Callable

from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    @staticmethod
    def _operate(a: Decimal, b: Decimal, func: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calc = Calculation.create(a, b, func)
        Calculations.add_calculation(calc)
        return calc.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._operate(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._operate(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._operate(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._operate(a, b, divide)
    