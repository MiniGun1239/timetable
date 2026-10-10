import json
from dataclasses import dataclass, field, asdict

from constants import CONFIG_DATA


@dataclass
class Config:
    days: list[str]
    periods: int
    school: str
    teachers: list
    classes: list
    subjects: list
    breaks: list[dict[str, int | str]] = field(init=False, repr=False)

    def __post_init__(self):
        self.breaks: list[dict[str, int | str]] = [
            {"after": self.periods // 3, "label": "First Break", "minutes": 15},
            {"after": self.periods*2 // 3, "label": "Second Break", "minutes": 15},
        ]

    def save(self):
        with open(CONFIG_DATA, "w") as conf_data:
            json.dump(asdict(self), conf_data, indent=2)
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
            conf_data["classes"],
            conf_data["subjects"]
        )

