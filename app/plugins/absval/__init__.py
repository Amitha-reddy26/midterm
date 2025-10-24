from app.commands import Command

class AbsvalCommand(Command):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def execute(self):
        return abs(self.a - self.b)
