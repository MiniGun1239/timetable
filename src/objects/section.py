import weakref
from email._header_value_parser import Section

from objects import Subject, subject


class Section:
    _instances = weakref.WeakSet()

    def __init__(
            self,
            id: int,
            grade: int,
            section: str,
            subject_ids: dict[str, int],
    ) -> None:
        self.id                         = id
        self.grade                      = grade
        self.section                    = section
        self.subjects: dict[str, int]   = subject_ids
        return

    def id(self):
        return self.id

    def get(self):
        return str(self.grade) + self.section

    def __repr__(self):
        return f"Section id: {self.id}, grade: {self.grade}, section: {self.section}"

    def serialize(self) -> dict:
        return {
            "id"        : self.id,
            "grade"     : self.grade,
            "section"   : self.section,
            "subjects"  : self.subjects
        }

    @classmethod
    def deserialize(cls, data: dict) -> Section:
        return cls(
            data["id"],
            data["grade"],
            data["section"],
            data["subjects"]
        )

    @classmethod
    def getInstances(cls):
        return cls._instances


def samples() -> dict[str, Section]:
    subjects: dict[str, Subject] = subject.samples()

    subject_ids = {}

    for key, sub in subjects:
        subject_ids[key] = sub.id

    return {
        "11A": Section(1, 11, 'A', subject_ids=subject_ids),
        "11B": Section(2, 11, 'B', subject_ids=subject_ids),
    }

