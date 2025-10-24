from app.commands import Command

class RootCommand(Command):
    def __init__(self, a=None, b=None):
        self.a = a  # base
        self.b = b  # root degree

    def execute(self):
        return self.a ** (1.0 / self.b)
