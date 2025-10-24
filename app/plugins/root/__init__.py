from app.commands import Command

class Root(Command):
    def execute(self, a, b):
        return a ** (1.0 / b)
