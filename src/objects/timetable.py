import weakref
from dataclasses import dataclass, asdict, field

from objects import Config


@dataclass
class Timetable:
    section: int
    rows: dict[str, list[int | None]]

    _instances: weakref.WeakSet = field(
        default_factory=weakref.WeakSet,
        init=False,
        repr=False
    )

    def __repr__(self) -> str:
        output = f"Timetable for Section {self.section}:\n"
        for day, row in self.rows.items():
            output += f"  {day}: {row}\n"
        return output

    def __post_init__(self):
        self._instances.add(self)

    def addRow(self, row: dict[str, list[int | None]]) -> bool:
        self.rows.update(row)
        return True

    def serialize(self):
        return asdict(self)

    @classmethod
    def deserialize(cls, data: dict[int, list[int | None]]) -> "Timetable":
        return cls(
            data["section"],
            data["rows"],
        )


def create(config: Config) -> Timetable:
    pass

