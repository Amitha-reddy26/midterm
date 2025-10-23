from decimal import Decimal
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

def test_add_calculation():
    Calculations.clear_history()
    calc = Calculation(Decimal('1'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc

def test_get_history():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.add_calculation(Calculation(Decimal('20.5'), Decimal('1.5'), subtract))
    history = Calculations.get_history()
    assert len(history) == 2

def test_clear_history():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.add_calculation(Calculation(Decimal('20.5'), Decimal('1.5'), subtract))
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20.5') and latest.b == Decimal('1.5')

def test_find_by_operation():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.add_calculation(Calculation(Decimal('20.5'), Decimal('1.5'), subtract))
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1

def test_get_latest_with_empty_history():
    Calculations.clear_history()
    assert Calculations.get_latest() is None
