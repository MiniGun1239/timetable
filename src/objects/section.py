from objects import Subject, subject


class Section:
    def __init__(
            self,
            id: int,
            grade: int,
            section: str,
            subjects: dict[str, Subject],
    ) -> None:
        self.id = id
        self.grade = grade
        self.section = section
        self.subjects: dict[str, Subject] = subjects
        return

    def id(self):
        return self.id

    def get(self):
        return str(self.grade) + self.section

    def __repr__(self):
        return f"Section id: {self.id}, grade: {self.grade}, section: {self.section}"

    # add more stuff here


def samples() -> dict[str, Section]:
    subjects = subject.samples()

    return {
        "11A": Section(1, 11, 'A', subjects),
        "11B": Section(2, 11, 'B', subjects),
    }

