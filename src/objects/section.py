import json
import weakref
from dataclasses import dataclass, field, asdict

from objects import subject
from constants import SECTION_DATA

Subject = subject.Subject


@dataclass
class Section:
    id: int
    grade: int
    section: str
    subjects: dict[str, int]

    _instances: weakref.WeakSet = field(default_factory=weakref.WeakSet, init=False, repr=False)

    def __post_init__(self):
        self._instances.add(self)

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

    for key, sub in subjects.items():
        subject_ids[key] = sub.id

    return {
        "11A": Section(1, 11, 'A', subjects=subject_ids),
        "11B": Section(2, 11, 'B', subjects=subject_ids),
    }


def save_all():
    all_secs = [section.serialize() for section in Section.getInstances()]

    with open(SECTION_DATA, "w", encoding="utf_8") as sec_data:
        json.dump(all_secs, sec_data, indent=2)


def load_all():
    with open(SECTION_DATA, "r", encoding="utf_8") as sec_data:
        all_sec: list[dict] = json.load(sec_data)

    for section in all_sec:
        Section.deserialize(section)


if __name__ == "__main__":
    sections = samples()
    for key, section in sections.items():
        print(f"{key}: {section}")

