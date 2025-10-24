from app.commands import Command

class Percentage(Command):
    def execute(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return (a / b) * 100
