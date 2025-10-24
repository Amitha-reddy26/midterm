from app.commands import Command

class Power(Command):
    def execute(self, a, b):
        return a ** b
