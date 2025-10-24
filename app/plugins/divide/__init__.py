from app import Command

class DivideCommand(Command):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def execute(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b

        if float(self.b) == 0:
            raise ValueError("Cannot divide by zero")

        return float(self.a) / float(self.b)
