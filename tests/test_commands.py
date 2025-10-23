import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommand

def test_add_command():
    add_command = AddCommand(3, 5)
    assert add_command.execute() == 8

def test_subtract_command():
    subtract_command = SubtractCommand(10, 4)
    assert subtract_command.execute() == 6

def test_multiply_command():
    multiply_command = MultiplyCommand(6, 7)
    assert multiply_command.execute() == 42

def test_divide_command():
    divide_command = DivideCommand(20, 5)
    assert divide_command.execute() == 4

def test_divide_by_zero():
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()

def test_menu_command():
    menu_command = MenuCommand()
    output = menu_command.execute()
    expected_output = "Available operations: add, subtract, multiply, divide\n"
    assert output == expected_output
