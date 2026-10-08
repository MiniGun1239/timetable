from enum import Enum, auto


class BackToBackPolicy(Enum):
    ANY = auto()
    FORCE = auto()
    FORBID = auto()

class Subject:
    def __init__(
            self,
            id: int,
            name: str,
            back2back: BackToBackPolicy = BackToBackPolicy.ANY,
            times_per_week: int = 1,
    ) -> None:


        self.id = id
        self.name = name

        self.back2back = back2back

        self.times_per_week = times_per_week
        return

    def __repr__(self):
        b2b_info = ", back2back: required" \
            if self.back2back.value == BackToBackPolicy.FORCE \
            else ", back2back: forbidden" \
            if self.back2back.value == BackToBackPolicy.FORBID \
            else ""

        return f"Subject id: {self.id}, name: {self.name}{b2b_info}, times per week: {self.times_per_week}"

    def is_back2back(self) -> bool:
        return True if self.back2back == BackToBackPolicy.FORCE else False

    def is_noback2back(self) -> bool:
        return True if self.back2back == BackToBackPolicy.FORBID else False

    # add more stuff idk wwhat tho


def samples() -> dict[int, Subject]:
    output = {}

    output.update(
        {"English1": Subject(1, "English", times_per_week=5)}
    )
    output.update(
        {"Math1": Subject(2, "Math / IP / PE", times_per_week=6)}
    )
    output.update(
        {"Physics1": Subject(3, "Physics", times_per_week=6)}
    )
    output.update(
        {"Chemistry1": Subject(4, "Chemistry", times_per_week=6)}
    )
    output.update(
        {"Biology1": Subject(5, "Bio / CS", times_per_week=6)}
    )
    output.update(
        {"Psychology1": Subject(6, "Psychology", times_per_week=3)}
    )
    output.update(
        {"PE1": Subject(7, "WB / PE", times_per_week=2)}
    )
    output.update(
        {"Biology LAB": Subject(8, "Bio / CS LAB", times_per_week=2)}
    )
    output.update(
        {"Physics LAB": Subject(9, "Physics LAB", times_per_week=2)}
    )
    output.update(
        {"Chemistry LAB": Subject(10, "Chemistry LAB", times_per_week=2)}
    )

    return output

if __name__ == "__main__":
    samples()

