from app.commands import Command

class PowerCommand(Command):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def execute(self):
        return self.a ** self.b
