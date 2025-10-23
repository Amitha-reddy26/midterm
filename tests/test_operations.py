from decimal import Decimal, getcontext, ROUND_HALF_UP
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

getcontext().prec = 3
getcontext().rounding = ROUND_HALF_UP

def test_operation_add():
    calculation = Calculation(Decimal('15'), Decimal('7'), add)
    assert calculation.perform() == Decimal('22')

def test_operation_subtract():
    calculation = Calculation(Decimal('15'), Decimal('7'), subtract)
    assert calculation.perform() == Decimal('8')

def test_operation_multiply():
    calculation = Calculation(Decimal('15'), Decimal('7'), multiply)
    assert calculation.perform() == Decimal('105')

def test_operation_divide():
    calculation = Calculation(Decimal('15'), Decimal('7'), divide)
    result = calculation.perform()
    expected_result = Decimal('2.14').quantize(Decimal('0.01'))
    assert result == expected_result

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('15'), Decimal('0'), divide)
        calculation.perform()
