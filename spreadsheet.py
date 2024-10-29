
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
            expression = value[1:]
            if expression.isdigit():
                return expression
            elif expression.startswith("'") and expression.endswith("'"):
                return expression[1:-1]
            else:
                return "#Error"  # Handle invalid formulas
        else:
            try:
                return int(value)
            except ValueError:
                return "#Error"  # Handle non-integer and improperly quoted strings

