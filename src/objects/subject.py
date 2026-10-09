from enum import Enum, auto


class BackToBackPolicy(Enum):
    ANY    = auto()
    FORCE  = auto()
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

    def b2b(self) -> BackToBackPolicy:
        return self.back2back.value

    # add more stuff idk wwhat tho


def samples() -> dict[str, Subject]:
    return {
        "English1"      : Subject(1,  "English",        times_per_week=5),
        "Math1"         : Subject(2,  "Math / IP / PE", times_per_week=6),
        "Physics1"      : Subject(3,  "Physics",        times_per_week=6),
        "Chemistry1"    : Subject(4,  "Chemistry",      times_per_week=6),
        "Biology1"      : Subject(5,  "Bio / CS",       times_per_week=6),
        "Psychology1"   : Subject(6,  "Psychology",     times_per_week=3),
        "PE1"           : Subject(7,  "WB / PE",        times_per_week=2),
        "Biology LAB"   : Subject(8,  "Bio / CS LAB",   times_per_week=2),
        "Physics LAB"   : Subject(9,  "Physics LAB",    times_per_week=2),
        "Chemistry LAB" : Subject(10, "Chemistry LAB",  times_per_week=2)
    }

if __name__ == "__main__":
    subjects = samples()
    for key, subject in subjects.items():
        print(f"{key}: {subject}")

