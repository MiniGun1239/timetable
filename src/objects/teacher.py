from objects import Section
from objects import subject, section


class Teacher:
    def __init__(
            self,
            id: int,
            name: str,
            subject_ids: list[int],
            section: Section | None = None,
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
    subjects = subject.samples()
    sections = section.samples()

    # ill just add my teacher names

    return {
        "Sabin": Teacher(1, "Sabin", subject_ids=[subjects["English1"].id], section=sections["11B"]),
        "Binesh": Teacher(2,  "Binesh", subject_ids=[subjects["Math1"].id]),
        "Mehenaz": Teacher(3, "Mehenaz", subject_ids=[subjects["Physics1"].id, subjects["Physics LAB"].id]),
        "Rani": Teacher(4, "Rani", subject_ids=[subjects["Chemistry1"].id, subjects["Chemistry LAB"].id]),
        "Divya": Teacher(5, "Divya", subject_ids=[subjects["Biology2"].id, subjects["Biology LAB"].id]),
        "Sadia": Teacher(6, "Sadia", subject_ids=[subjects["Psychology1"].id]),
        "Mujeeb": Teacher(7, "Mujeeb", subject_ids=[subjects["PE1"].id]),
    }

