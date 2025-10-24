from app.commands import Command

class Modulus(Command):
    def execute(self, a, b):
        if b == 0:
            return "Error: Cannot perform modulus by zero"
        return a % b
