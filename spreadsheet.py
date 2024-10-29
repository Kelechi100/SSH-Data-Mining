
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.startswith("'") and value.endswith("'"):
            return value
        elif value.startswith("="):
            # Evaluate the expression following '='
            expression = value[1:]
            if expression.isdigit():
                return expression  # Return the string representation of the digit
            elif expression.startswith("'") and expression.endswith("'"):
                return expression[1:-1]  # Remove the surrounding quotes
            return value  # Return the original formula if not a valid expression
        else:
            try:
                return int(value)
            except ValueError:
                return "#Error"

