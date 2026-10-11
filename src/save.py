from objects import section, subject, teacher, config, timetable


def save_all():
    section.save_all()
    subject.save_all()
    teacher.save_all()
    config.save()
    timetable.save_all()
