import json
from dataclasses import dataclass, asdict
from typing import ClassVar

from constants import TEACHER_DATA
from objects import section, subject

@dataclass
class Teacher:
    id: int
    name: str
    subjects: list[int]
    section: int | None = None

    # --- BASICS ---
    _instances: ClassVar[list] = []

    def __post_init__(self):
        if self not in self._instances:
            self._instances.append(self)

    def __repr__(self):
        return f"{self.name}: id={self.id}, subjects={self.subjects}{f", section = {self.section}" if self.section else ""}"

    @classmethod
    def getInstances(cls):
        return cls._instances


    # --- SAVING AND LOADING ---
    # --- Core ---
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

    def append(self):
        with open(TEACHER_DATA, "r", encoding="utf-8") as teach_data:
            all_teachs: list[dict] = json.load(teach_data)

        all_teachs.append(self.serialize())

        self.__class__.save_all()

    # --- SAVE AND LOAD ALL
    @classmethod
    def save_all(cls):
        all_teachs = [teacher.serialize() for teacher in cls.getInstances()]

        with open(TEACHER_DATA, "w", encoding="utf-8") as teach_data:
            json.dump(all_teachs, teach_data, indent=2)

    @classmethod
    def load_all(cls):
        with open(TEACHER_DATA, "r", encoding="utf-8") as teach_data:
            all_teachs: list[dict] = json.load(teach_data)

        for teacher in all_teachs:
            Teacher.deserialize(teacher)
        return


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
                subjects["Physics LAB1"].id
            ]
        ),
        "Rani"   : Teacher(
            4, "Rani",
            subjects=[
                subjects["Chemistry1"   ].id,
                subjects["Chemistry LAB1"].id
            ]
        ),
        "Divya"  : Teacher(
            5, "Divya",
            subjects=[
                subjects["Biology1"].id,
                subjects["Biology LAB1"].id
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


if __name__ == "__main__":
    Teacher.load_all()
    teachers = Teacher.getInstances()

    for teacher in teachers:
        print(f"{teacher}")

