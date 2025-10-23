from app.commands import Command

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero") 
        result = self.a / self.b
        print(f"DivideCommand: {self.a} / {self.b} = {result}")
        return result
    
