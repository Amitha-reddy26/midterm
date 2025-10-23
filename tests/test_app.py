import pytest
from app import App
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_app_start_exit_command(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as exit_exception:
        app.start()
    assert exit_exception.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_register_and_execute_multiply_command(capsys):
    handler = CommandHandler()
    multiply_command = MultiplyCommand(6, 7)
    handler.register_command("multiply", multiply_command)
    result = handler.execute_command("multiply")
    captured = capsys.readouterr()
    assert captured.out == "MultiplyCommand: 6 * 7 = 42\n"
    assert result == 42

def test_register_and_execute_divide_command(capsys):
    handler = CommandHandler()
    divide_command = DivideCommand(10, 2)
    handler.register_command("divide", divide_command)
    result = handler.execute_command("divide")
    captured = capsys.readouterr()
    assert captured.out == "DivideCommand: 10 / 2 = 5.0\n"
    assert result == 5.0

def test_divide_by_zero():
    handler = CommandHandler()
    divide_command = DivideCommand(10, 0)
    handler.register_command("divide_zero", divide_command)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        handler.execute_command("divide_zero")

def test_register_and_execute_add_command(capsys):
    handler = CommandHandler()
    add_command = AddCommand(2, 3)
    handler.register_command("add", add_command)
    result = handler.execute_command("add")
    captured = capsys.readouterr()
    assert captured.out == "AddCommand: 2 + 3 = 5\n"
    assert result == 5

def test_register_and_execute_subtract_command(capsys):
    handler = CommandHandler()
    subtract_command = SubtractCommand(5, 2)
    handler.register_command("subtract", subtract_command)
    result = handler.execute_command("subtract")
    captured = capsys.readouterr()
    assert captured.out == "SubtractCommand: 5 - 2 = 3\n"
    assert result == 3

def test_execute_nonexistent_command():
    handler = CommandHandler()
    result = handler.execute_command("nonexistent")
    expected_message = "No such command: nonexistent"
    assert result == expected_message
