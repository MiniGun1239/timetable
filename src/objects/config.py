class Config:
    def __init__(
            self,
            days: list[str],
            periods: int,
            school: str,
            teachers: list,
            classes: list,
            subjects: list
    ) -> None:
        self.school = school
        self.period_per_day = periods
        self.days = days
        self.breaks = [
            {"after": periods // 3, "label": "First Break", "minutes": 15},
            {"after": periods*2 // 3, "label": "Second Break", "minutes": 15},
        ]
        self.teachers = teachers
        self.classes = classes
        self.subjects = subjects
        return

    # more stuff needs to be added here

