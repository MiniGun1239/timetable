from objects.section import Section


class Timetable:
    def __init__(self, section: Section) -> None:
        self.section = section
        self.order = {}

