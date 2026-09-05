from Types import DataType


class GoodStudentsCalculator:

    def __init__(self, data: DataType) -> None:
        self.data = data

    def calculate(self) -> int:
        count = 0

        for subjects in self.data.values():
            if all(score >= 76 for _, score in subjects):
                count += 1

        return count
