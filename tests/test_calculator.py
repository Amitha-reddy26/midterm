'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    assert Calculator.add(1, 2) == 3

def test_subtraction():
    assert Calculator.subtract(1, 2) == -1

def test_divide():
    assert Calculator.divide(1, 2) == 0.5

def test_multiply():
    assert Calculator.multiply(1, 2) == 2
