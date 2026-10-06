class Subject:
    def __init__(
            self,
            id: int,
            name: str,
            back2back: bool = False,
            noback2back: bool = False
    ) -> None:
        if back2back and noback2back:
            print("Invalid, cant have both back to back and not back to back")
            raise ValueError

        self.id = id
        self.name = name

        self.back2back = back2back
        self.noback2back = noback2back
        return

    def print(self):
        b2b_info = f"{', back2back: yes' if self.back2back else ', noback2back: yes' if self.noback2back else ''}"

        return f"Subject id: {self.id}, name: {self.name}{b2b_info}"

    def is_back2back(self) -> bool:
        return self.back2back

    def is_noback2back(self) -> bool:
        return self.noback2back

    # add more stuff idk wwhat tho

