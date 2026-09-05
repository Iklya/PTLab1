import xml.etree.ElementTree as ET

from DataReader import DataReader
from Types import DataType


class XMLDataReader(DataReader):

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        students: DataType = {}

        for student in root.findall("student"):
            name = student.get("name")
            students[name] = []

            for subject in student.findall("subject"):
                subject_name = subject.get("name")
                score = int(subject.text)

                students[name].append(
                    (subject_name, score)
                )

        return students
