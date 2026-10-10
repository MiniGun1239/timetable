from dataclasses import dataclass, asdict

from objects import Config, Section


@dataclass
class Timetable:
    config: Config
    section: Section
    rows: dict[str, list[int | None]]

    def addRow(self, row: dict[str, list[int | None]]) -> bool:
        self.rows.update(row)
        return True

    def serialize(self):
        return asdict(self)


def create(config: Config) -> Timetable:
    pass

