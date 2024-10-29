
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        if cell in self._evaluating:
            raise ValueError("Circular dependency detected")
        self._evaluating.add(cell)
        try:
            value = self.get(cell)
            try:
                return int(value)
            except ValueError:
                return "#Error"
        finally:
            self._evaluating.remove(cell)

