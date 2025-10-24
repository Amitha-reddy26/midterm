from app.commands import Command

class Absolute(Command):
    def execute(self, a, b):
        return abs(a - b)
