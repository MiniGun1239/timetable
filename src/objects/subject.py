class Subject:
    def __init__(
            self,
            id: int,
            name: str,
            back2back: bool = False,
            noback2back: bool = False,
            times_per_week: int = 1,
    ) -> None:
        if back2back and noback2back:
            print("Invalid, cant have both back to back and not back to back")
            raise ValueError

        self.id = id
        self.name = name

        self.back2back = back2back
        self.noback2back = noback2back

        self.times_per_week = times_per_week
        return

    def print(self):
        b2b_info = f"{', back2back: yes' if self.back2back else ', noback2back: yes' if self.noback2back else ''}"

        return f"Subject id: {self.id}, name: {self.name}{b2b_info}, times per week: {self.times_per_week}"

    def is_back2back(self) -> bool:
        return self.back2back

    def is_noback2back(self) -> bool:
        return self.noback2back

    # add more stuff idk wwhat tho


def samples() -> list[Subject]:
    output = []

    output.append(
        Subject(1, "English", times_per_week=5)
    )
    output.append(
        Subject(2, "Math / IP / PE", times_per_week=6)
    )
    output.append(
        Subject(3, "Physics", times_per_week=6)
    )
    output.append(
        Subject(4, "Chemistry", times_per_week=6)
    )
    output.append(
        Subject(5, "Bio / CS", times_per_week=6)
    )
    output.append(
        Subject(6, "Psychology", times_per_week=3)
    )
    output.append(
        Subject(7, "WB / PE", times_per_week=2)
    )
    output.append(
        Subject(8, "Bio / CS LAB", times_per_week=2)
    )
    output.append(
        Subject(9, "Physics LAB", times_per_week=2)
    )
    output.append(
        Subject(10, "Chemistry LAB", times_per_week=2)
    )

    periods = 0
    for subject in output:
        periods += subject.times_per_week

    print(f"Subjects: {periods}")

    return output

if __name__ == "__main__":
    samples()

