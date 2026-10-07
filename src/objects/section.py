from objects import Subject, subject


class Section:
    def __init__(
            self,
            id: int,
            grade: int,
            section: str,
            subjects: list[Subject],
    ) -> None:
        self.id = id
        self.grade = grade
        self.section = section
        self.subjects: list[Subject] = subjects
        return

    def id(self):
        return self.id

    def get(self):
        return str(self.grade) + self.section

    def print(self):
        return f"Section id: {self.id}, grade: {self.grade}, section: {self.section}"

    # add more stuff here


def sample() -> list[Section]:
    output = []

    subjects = subject.samples()

    output.append(
        Section(1, 11, "A", subjects)
    )
    output.append(
        Section(2, 11, "B", subjects)
    )

    return output

