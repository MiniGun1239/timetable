import weakref
from dataclasses import dataclass, field, asdict

from . import Subject, subject


@dataclass
class Section:
    id: int
    grade: int
    section: str
    subjects: dict[str, int]

    _instances: weakref.WeakSet = field(default_factory=weakref.WeakSet, init=False, repr=False)

    def get(self):
        return str(self.grade) + self.section

    def serialize(self) -> dict:
        return asdict(self)

    @classmethod
    def deserialize(cls, data: dict) -> "Section":
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
        "11A": Section(1, 11, 'A', subjects=subject_ids),
        "11B": Section(2, 11, 'B', subjects=subject_ids),
    }

if __name__ == "__main__":
    sections = samples()
    for section in sections:
        print(section)

