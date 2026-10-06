from objects.config import Config
from objects.subject import Subject
from objects.section import Section
from objects.teacher import Teacher

def all_test():
    section_test()
    subject_test()
    teacher_test()
    config_test()
    pass


def config_get():
    pass


def section_get():
    pass


def teacher_get(subjects: list[Subject], section: list[Section]):
    output = []

    for subject, i in subjects, range(len(subjects)):
        teacher = Teacher(
            id=i,
            name=f"Teacher{str(i)}",
            subject_ids=[subject.id],
            section=section[i]
        )


def subject_get() -> list[Subject]:
    output = []

    english1 = Subject(
        id=1,
        name="English"
    )
    output.append(english1)

    math1 = Subject(
        id=2,
        name="Math"
    )
    output.append(math1)

    science1 = Subject(
        id=3,
        name="Science"
    )
    output.append(science1)

    english2 = Subject(
        id=4,
        name="English"
    )
    output.append(english2)

    return output

