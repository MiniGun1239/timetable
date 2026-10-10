import weakref
from dataclasses import dataclass, field, asdict

from . import section, subject

@dataclass
class Teacher:
    id: int
    name: str
    subjects: list[int]
    section: int | None = None

    _instances: weakref.WeakSet = field(default_factory=weakref.WeakSet, init=False, repr=False)

    def __post_init__(self):
        self._instances.add(self)

    def serialize(self) -> dict:
        return asdict(self)

    @classmethod
    def deserialize(cls, data: dict) -> "Teacher":
        return cls(
            data["id"],
            data["name"],
            subjects=data["subjects"],
            section=data.get("section")
        )

    @classmethod
    def getInstances(cls):
        return cls._instances


def samples():
    subjects = subject.samples()
    sections = section.samples()

    # ill just add my teacher names

    return {
        "Sabin"  : Teacher(
            1, "Sabin",
            subjects=[subjects["English1"].id],
            section=sections["11B"].id
        ),
        "Binesh" : Teacher(
            2, "Binesh",
            subjects=[subjects["Math1"].id]
        ),
        "Mehenaz": Teacher(
            3, "Mehenaz",
            subjects=[
                subjects["Physics1"   ].id,
                subjects["Physics LAB"].id
            ]
        ),
        "Rani"   : Teacher(
            4, "Rani",
            subjects=[
                subjects["Chemistry1"   ].id,
                subjects["Chemistry LAB"].id
            ]
        ),
        "Divya"  : Teacher(
            5, "Divya",
            subjects=[
                subjects["Biology2"].id,
                subjects["Biology LAB"].id
            ]
        ),
        "Sadia"  : Teacher(
            6, "Sadia",
            subjects=[subjects["Psychology1"].id]
        ),
        "Mujeeb" : Teacher(
            7, "Mujeeb",
            subjects=[subjects["PE1"].id]
        ),
    }


def save_all():
    all_teachs = [teacher.serialize() for teacher in Teacher.getInstances()]

    with open(TEACHER_DATA, "w", encoding="utf-8") as teach_data:
        json.dump(all_teachs, teach_data, indent=2)

def load_all():
    with open(TEACHER_DATA, "r", encoding="utf-8") as teach_data:
        all_teachs: list[dict] = json.load(teach_data)


if __name__ == "__main__":
    for teacher in samples():
        print(teacher)

