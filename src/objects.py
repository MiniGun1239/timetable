class Period:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        return

    # add more stuff idk wwhat tho


class Section:
    def __init__(
            self,
            id: int,
            grade: int,
            section: str,
            back2back: bool = False,
            nobacktoback: bool = False
    ) -> None:
        if back2back and nobacktoback:
            print("Invalid, cant have both back to back and not back to back")
            raise ValueError

        self.id = id
        self.grade = grade
        self.section = section
        self.back2back = back2back
        self.nobacktoback = nobacktoback
        return

    # add more stuff here


class Teacher:
    def __init__(
            self,
            id: int,
            name: str,
            subjects: list,
            section: Section):
        self.id = id
        self.name = name
        self.subjects = subjects
        self.section = section
        return

    # add somehow routing this


class Config:
    def __init__(
            self,
            periods: int,
            school: str,
            teachers: list,
            classes: list,
            subjects: list
    ):
        self.school = school
        self.period_per_day = periods
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        self.breaks = [
            {"after": periods // 3, "label": "First Break", "minutes": 15},
            {"after": periods*2 // 3, "label": "Second Break", "minutes": 15},
        ]
        self.teachers = teachers
        self.classes = classes
        self.subjects = subjects
        return

