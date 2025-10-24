from app.commands import Command

class Menu(Command):
    def execute(self, a=None, b=None):
        return (
            "\nAvailable operations:\n"
            "  • add         → Adds two numbers\n"
            "  • subtract    → Subtracts second number from first\n"
            "  • multiply    → Multiplies two numbers\n"
            "  • divide      → Divides first number by second\n"
            "  • modulus     → Returns the remainder of division\n"
            "  • percentage  → Percentage of a with respect to b\n"
            "  • absolute    → Absolute difference between a and b\n"
            "  • power       → Raises first number to the power of second\n"
            "  • root        → Takes the nth root (b-th root of a)\n"
            "  • menu        → Displays this list\n"
            "  • exit        → Exits the application\n"
        )
