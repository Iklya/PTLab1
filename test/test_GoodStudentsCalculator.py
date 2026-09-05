from src.GoodStudentsCalculator import GoodStudentsCalculator
from src.Types import DataType


class TestGoodStudentsCalculator:

    def test_calculate(self) -> None:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 61)
            ],
            "Сидоров Сидор Сидорович": [
                ("математика", 76),
                ("программирование", 80),
                ("история", 90)
            ]
        }

        result = GoodStudentsCalculator(data).calculate()

        assert result == 2

    def test_no_good_students(self) -> None:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 75),
                ("программирование", 90)
            ],
            "Петров Петр Петрович": [
                ("математика", 60),
                ("химия", 70)
            ]
        }

        result = GoodStudentsCalculator(data).calculate()

        assert result == 0

    def test_score_76_is_good(self) -> None:
        data: DataType = {
            "Сидоров Сидор Сидорович": [
                ("математика", 76),
                ("программирование", 76),
                ("литература", 76)
            ]
        }

        result = GoodStudentsCalculator(data).calculate()

        assert result == 1

    def test_score_76_is_good(self) -> None:
        data: DataType = {
            "Сидоров Сидор Сидорович": [
                ("математика", 76),
                ("программирование", 76),
                ("литература", 76)
            ]
        }

        result = GoodStudentsCalculator(data).calculate()

        assert result == 1
