import weakref
from dataclasses import dataclass

from objects import subject, section


class Teacher:
    _instances = weakref.WeakSet()

    def __init__(
            self,
            id: int,
            name: str,
            subject_ids: list[int],
            section_id: int | None = None,
    ) -> None:
        self.id         = id
        self.name       = name
        self.subjects   = subject_ids
        self.section    = section_id
        return

    def __repr__(self):
        return f"Teacher id: {self.id}, name: {self.name}, section: {self.section}"

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "subjects": self.subjects,
            "section": self.section
        }

    @classmethod
    def deserialize(cls, data: dict):
        return cls(
            data["id"],
            data["name"],
            data["subjects"],
            data["section"]
        )

    @classmethod
    def getInstances(cls):
        return cls._instances


def samples():
    subjects = subject.samples()
    sections = section.samples()

    # ill just add my teacher names

    return {
        "Sabin"     : Teacher(1, "Sabin",   subject_ids=[subjects["English1"   ].id                                ], section_id=sections["11B"].id()),
        "Binesh"    : Teacher(2, "Binesh",  subject_ids=[subjects["Math1"      ].id                                ]),
        "Mehenaz"   : Teacher(3, "Mehenaz", subject_ids=[subjects["Physics1"   ].id , subjects["Physics LAB"  ].id ]),
        "Rani"      : Teacher(4, "Rani",    subject_ids=[subjects["Chemistry1" ].id , subjects["Chemistry LAB"].id ]),
        "Divya"     : Teacher(5, "Divya",   subject_ids=[subjects["Biology2"   ].id , subjects["Biology LAB"  ].id ]),
        "Sadia"     : Teacher(6, "Sadia",   subject_ids=[subjects["Psychology1"].id                                ]),
        "Mujeeb"    : Teacher(7, "Mujeeb",  subject_ids=[subjects["PE1"        ].id                                ]),
    }

