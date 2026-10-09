from objects import Config, Section


class Timetable:
    def __init__(self, section: Section) -> None:
        self.section = section
        self.order = {}


def create(config: Config) -> Timetable:
    pass

