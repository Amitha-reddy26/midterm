from app.commands import Command

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a + self.b
        print(f"AddCommand: {self.a} + {self.b} = {result}")
        return result
