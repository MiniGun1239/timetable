class Teacher:
    def __init__(self, id, name, subjects: list):
        self.id = id
        self.name = name
        self.subjects = subjects
        return

    # add somehow routing this


class Period:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        return

    # add more stuff idk wwhat tho


class Section:
    def __init__(self, id, grade, section, back2back, nobacktoback = False):
        if back2back and nobacktoback:
            print("Invalid, cant have both back to back and not back to back")
            return

        self.id = id
        self.grade = grade
        self.section = section
        self.back2back = back2back
        self.nobacktoback = nobacktoback
        return

    # add more stuff here

class Config:
    def __init__(self, teachers: list, classes: list, subjects: list):
        self.school = "Hack Club Institute"
        self.period_per_day = 6
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        self.breaks = [
            {"after": 2, "type": "First Break", "time": 15},
            {"after": 4, "type": "Second Break", "time": 15},
        ]
        self.teachers = teachers
        self.classes = classes
        self.subjects = subjects
        return

