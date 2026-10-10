import json
import weakref
from dataclasses import dataclass, field, asdict
from enum import Enum

from constants import SUBJECT_DATA


class BackToBackPolicy(str, Enum):
    ANY    = "ANY"
    FORCE  = "FORCE"
    FORBID = "FORBID"


@dataclass
class Subject:
    id: int
    name: str
    back2back: BackToBackPolicy = BackToBackPolicy.ANY
    times_per_week: int = 1

    _instances: weakref.WeakSet = field(default_factory=weakref.WeakSet, init=False, repr=False)

    def __post_init__(self):
        self._instances.add(self)

    def __repr__(self):
        b2b_info = ", back2back: required" \
            if self.back2back.value == BackToBackPolicy.FORCE \
            else ", back2back: forbidden" \
            if self.back2back.value == BackToBackPolicy.FORBID \
            else ""

        return f"Subject id: {self.id}, name: {self.name}{b2b_info}, times per week: {self.times_per_week}"

    def b2b(self) -> BackToBackPolicy:
        return self.back2back

    def serialize(self):
        data = asdict(self)
        data["back2back"] = self.back2back.value
        return data

    @classmethod
    def deserialize(cls, data: dict):
        return cls(
            data["id"],
            data["name"],
            back2back=BackToBackPolicy(data["back2back"]),
            times_per_week=data["times_per_week"]
        )

    @classmethod
    def getInstances(cls):
        return cls._instances


def samples() -> dict[str, Subject]:
    return {
        "English1"       : Subject(1,  "English",       times_per_week=5),
        "Math1"          : Subject(2,  "Math",          times_per_week=6),
        "Physics1"       : Subject(3,  "Physics",       times_per_week=6),
        "Chemistry1"     : Subject(4,  "Chemistry",     times_per_week=6),
        "Biology1"       : Subject(5,  "Biology",       times_per_week=6),
        "Psychology1"    : Subject(6,  "Psychology",    times_per_week=3),
        "PE1"            : Subject(7,  "PE",            times_per_week=2, back2back=BackToBackPolicy.FORBID ),
        "Biology LAB1"   : Subject(8,  "Biology LAB",   times_per_week=2, back2back=BackToBackPolicy.FORCE  ),
        "Physics LAB1"   : Subject(9,  "Physics LAB",   times_per_week=2, back2back=BackToBackPolicy.FORCE  ),
        "Chemistry LAB1" : Subject(10, "Chemistry LAB", times_per_week=2, back2back=BackToBackPolicy.FORCE  ),
    }


def save_all():
    all_subs = [subject.serialize() for subject in Subject.getInstances()]

    with open(SUBJECT_DATA, "w", encoding="utf_8") as sub_data:
        json.dump(all_subs, sub_data, indent=2)


def load_all():
    with open(SUBJECT_DATA, "r", encoding="utf_8") as sub_data:
        all_subs: list[dict] = json.load(sub_data)

    for subject in all_subs:
        Subject.deserialize(subject)


if __name__ == "__main__":
    subjects = samples()
    for key, subject in subjects.items():
        print(f"{key}: {subject}")

