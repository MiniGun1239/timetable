from dataclasses import dataclass, asdict, field
from ortools.sat.python import cp_model

from objects import config

Config = config.Config


@dataclass
class Timetable:
    section: int
    rows: dict[str, list[int | None]]

    _instances: list = field(
        default_factory=list,
        init=False,
        repr=False
    )

    def __repr__(self) -> str:
        section_name = self.section

        for section in Section.getInstances():
            if section.id == self.section:
                section_name = section.get()
                break

        output = f"Timetable for {section_name}:\n"
        for day, row in self.rows.items():
            output += f"  {day}: {row}\n"
        return output

    def __post_init__(self):
        self._instances.append(self)

    def addRow(self, row: dict[str, list[int | None]]) -> bool:
        self.rows.update(row)
        return True

    def serialize(self):
        return asdict(self)

    @classmethod
    def deserialize(cls, data: dict) -> "Timetable":
        return cls(
            data["section"],
            data["rows"],
        )


def create(config: Config) -> Timetable:
    pass

