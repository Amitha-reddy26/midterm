from app.commands import Command

class ModulusCommand(Command):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            return "Error: Cannot divide by zero"
        return self.a % self.b
