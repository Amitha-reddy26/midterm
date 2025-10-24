from app.commands import Command

class Subtract(Command):
    def execute(self, a, b):
        return a - b
