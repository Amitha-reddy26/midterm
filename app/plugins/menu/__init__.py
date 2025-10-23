import sys
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        return "Available operations: add, subtract, multiply, divide\n"  

# pylint: disable=R0903
