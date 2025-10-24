from app.commands import Command

class MenuCommand(Command):
    def execute(self, a=None, b=None):
        return "Available operations: add, subtract, multiply, divide\n"
