from objects import subject, Subject


class Teacher:
    def __init__(
            self,
            id: int,
            name: str,
            subject_ids: list[int],
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


def samples():
    output = []

    subjects = subject.samples()

    # ill just add my teacher names

    output.append(
        Teacher(1, "Sabin da goat", [subjects[0].id], )
    )