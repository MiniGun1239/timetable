class Section:
    def __init__(
            self,
            id: int,
            grade: int,
            section: str,
    ) -> None:
        self.id = id
        self.grade = grade
        self.section = section
        return

    def id(self):
        return self.id

    def get(self):
        return str(self.grade) + self.section

    def print(self):
        return f"Section id: {self.id}, grade: {self.grade}, section: {self.section}"

    # add more stuff here


class Subject:
    def __init__(
            self,
            id: int,
            name: str,
            sections: list[Section],
            back2back: bool = False,
            noback2back: bool = False
    ) -> None:
        if back2back and noback2back:
            print("Invalid, cant have both back to back and not back to back")
            raise ValueError

        self.id = id
        self.name = name
        self.sections = sections

        self.back2back = back2back
        self.noback2back = noback2back
        return

    def print(self):
        b2b_info = f"{', back2back: yes' if self.back2back else ', noback2back: yes' if self.noback2back else ''}"
        sections = []
        for i in self.sections:
            sections.append(i.get())

        return f"Subject id: {self.id}, name: {self.name}, sections: {sections}{b2b_info}"

    def is_back2back(self) -> bool:
        return self.back2back

    def is_noback2back(self) -> bool:
        return self.noback2back

    # add more stuff idk wwhat tho


class Teacher:
    def __init__(
            self,
            id: int,
            name: str,
            subject_ids: list,
            section: Section
    ) -> None:
        self.id = id
        self.name = name
        self.subjects = subject_ids
        self.section = section
        return

    def print(self):
        return f"Teacher id: {self.id}, name: {self.name}, section: {self.section.get()}"

    # add somehow routing this


class Config:
    def __init__(
            self,
            periods: int,
            school: str,
            teachers: list,
            classes: list,
            subjects: list
    ) -> None:
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

