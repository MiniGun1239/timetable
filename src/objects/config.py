import json
from dataclasses import dataclass, field, asdict
from typing import ClassVar

from constants import CONFIG_DATA
from objects import section, subject, teacher


@dataclass
class Config:
    days: list[str]
    periods: int
    school: str
    teachers: list
    sections: list
    subjects: list
    breaks: list[dict[str, int | str]] = field(init=False, repr=False)

    _instances: ClassVar[list] = []

    def __post_init__(self):
        self.breaks: list[dict[str, int | str]] = [
            {"after": self.periods // 3, "label": "First Break", "minutes": 15},
            {"after": self.periods*2 // 3, "label": "Second Break", "minutes": 15},
        ]
        self._instances.append(self)


    def save_this(self):
        with open(CONFIG_DATA, "w") as conf_data:
            json.dump(asdict(self), conf_data, indent=2)
        return

    @classmethod
    def save(cls):
        with open(CONFIG_DATA, "w") as conf_data:
            json.dump(asdict(cls.getInstance()), conf_data, indent=2)
        return

    @classmethod
    def load(cls) -> "Config":
        with open(CONFIG_DATA, "r") as conf_data:
            conf_data: dict = json.load(conf_data)
        return cls(
            conf_data["days"],
            conf_data["periods"],
            conf_data["school"],
            conf_data["teachers"],
            conf_data["sections"],
            conf_data["subjects"]
        )

    @classmethod
    def getInstance(cls) -> "Config":
        return cls._instances[-1]

    @classmethod
    def getInstances(cls) -> list:
        return cls._instances


def sample():
    teachers = teacher.samples()
    sections = list(section.samples().values())
    subjects = list(subject.samples().values())

    days = ["mon", "tue", "wed", "thu", "fri"]
    school_name = "Hack Club Institute of Hacking"

    return Config(
        days=days,
        periods=8,
        school=school_name,
        teachers=teachers,
        sections=sections,
        subjects=subjects,
    )


if __name__ == "__main__":
    config = Config.load()

    print(config)
    Config.save()

