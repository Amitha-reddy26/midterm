from app import Command

class MultiplyCommand(Command):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def execute(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        return float(self.a) * float(self.b)
