from app.commands import Command

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a * self.b
        print(f"MultiplyCommand: {self.a} * {self.b} = {result}")
        return result
