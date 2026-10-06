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