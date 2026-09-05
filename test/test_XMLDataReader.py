from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    def test_read(self, tmpdir) -> None:
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<root>
    <student name="Иванов Иван Иванович">
        <subject name="математика">67</subject>
        <subject name="литература">100</subject>
        <subject name="программирование">91</subject>
    </student>
    <student name="Петров Петр Петрович">
        <subject name="математика">78</subject>
        <subject name="химия">87</subject>
        <subject name="социология">61</subject>
    </student>
</root>
"""

        expected: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }

        filepath = tmpdir.join("data.xml")
        filepath.write_text(xml_content, encoding="utf-8")

        result = XMLDataReader().read(str(filepath))

        assert result == expected

    def test_read_empty_root(self, tmpdir) -> None:
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
        <root>
        </root>
        """

        filepath = tmpdir.join("empty.xml")
        filepath.write_text(xml_content, encoding="utf-8")

        result = XMLDataReader().read(str(filepath))

        assert result == {}

    def test_read_single_student(self, tmpdir) -> None:
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
        <root>
            <student name="Сидоров Сидор Сидорович">
                <subject name="математика">76</subject>
            </student>
        </root>
        """

        expected: DataType = {
            "Сидоров Сидор Сидорович": [
                ("математика", 76)
            ]
        }

        filepath = tmpdir.join("single.xml")
        filepath.write_text(xml_content, encoding="utf-8")

        result = XMLDataReader().read(str(filepath))

        assert result == expected
