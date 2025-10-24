from app.commands import Command

class Multiply(Command):
    def execute(self, a, b):
        return a * b
