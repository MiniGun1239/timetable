from ortools.sat.python import cp_model

# idrk, this might be bad code
# i dont usually write python, actually never
# worst code ever??

def generate_schedule(data):
    days = data.get("days", [])
    periods = data.get("periodsPerDay", 0)
    grades = data.get("grades", [])
    subjects = data.get("subjects", [])
    teachers = data.get("teachers", [])
    requirements = data.get("assignments", [])

    if len(days) == 0:
        raise ValueError("Choose atleast 1 teaching day")

    if type(periods) is not int or periods < 1:
        raise ValueError("Periods must be positive bruh")

    classes = []

    for grade in grades:
        grade_name = str(grade.get("name", "")).strip()

        for section in grade.get("sections", []):
            section_name = str(section).strip()

            if grade_name == "" or section_name == "":
                raise ValueError("Write the grade and section gng")

            class_name = grade_name + "-" + section_name
            classes.append(class_name)

    if len(classes) == 0:
        raise ValueError("Add a class")

    if len(subjects) == 0 or len(teachers) == 0:
        raise ValueError("Add atleast 1 subject and teacher")

    allowed_lessons = {}

    for class_name in classes:
        allowed_lessons[class_name] = []

    for requirement in requirements:
        class_name = requirement.get("className")
        subject_id = requirement.get("subjectId")
        teacher_id = requirement.get("teacherId")
        minimum = requirement.get("minimumPerWeek")

        if class_name not in classes:
            raise ValueError("Weekly requirement has an unknown class")

        subject_exists = False
        for subject in subjects:
            if subject.get("id") == subject_id:
                subject_exists = True

        teacher_exists = False
        for teacher in teachers:
            if teacher.get("id") == teacher_id:
                if subject_id in teacher.get("subjectIds", []):
                    teacher_can_teach = True

        if not subject_exists or not teacher_can_teach:
            raise ValueError("Weekly requirement has unknown subject or a teacher that cant teach the subject you chose")

        if type(minimum) is not int or minimum < 1:
            raise ValueError("Minimum hours must be a positive number")

        combination = (subject_id, teacher_id)

        if combination not in allowed_lessons[class_name]:
            allowed_lessons[class_name].append(combination)

    # lowk so many cases
    for class_name in classes:
        if len(allowed_lessons[class_name]) == 0:
            raise ValueError("Add weekly requirement for " + class_name + ".")

    model = cp_model.CpModel()

    lessons = []

    for class_name in classes:
        for day in days:
            for period in range(periods):
                for combination in allowed_lessons[class_name]:
                    subject_id = combination[0]
                    teacher_id = combination[1]

                    lessons_variable = model.NewBoolVar(
                        "lesson_" + str(len(lessons))
                    )

                    lessons.append({
                        "class": class_name,
                        "day": day,
                        "period": period,
                        "subject": subject_id,
                        "teacher": teacher_id,
                        "variable": lessons_variable
                    })
 # is this the worst code ever??
    for class_name in classes:
        for day in days:
            for period in range(periods):
                choices = []

                for lesson in lessons:
                    if (lesson["class"] == class_name and lesson["day"] == day and lesson["period"] == period):
                            choices.append(lesson["variable"])

                model.Add(sum(choices) == 1)
 # yea, wth am i doing??
    for teacher in teachers:
        teacher_id = teacher.get("id")

        for day in days:
            for period in range(periods):
                teacher_lessons = []

                for lesson in lessons:
                    if (lesson["teacher"] == teacher_id and lesson["day"] == day and lesson["period"] == period):
                        teacher_lessons.append(lesson["variable"])

                model.Add(sum(teacher_lessons) <= 1)

    for teacher in teachers:
        teacher_id = teacher.get("id")
        daily_limit = teacher.get("maxPerDay", periods)
    # python is so weird, idk just too much like english
        if type(daily_limit) is not int or daily_limit < 0:
            raise ValueError("Enter valid daily limit for the teachers")

        for day in days:
            teacher_day = []

            for lesson in lessons:
                if lesson["teacher"] == teacher_id and lesson["day"] == day:
                    teacher_day.append(lesson["variable"])

            model.Add(sum(teacher_day) <= daily_limit)

    for subject in subjects:
        if subject.get("noBackToBack") is True:
            subject_id = subject.get("id")

            for class_name in classes:
                for day in days:
                    for period in range(periods - 1):
                        first_period = []
                        next_period = []

                        for lesson in lessons:
                            if (lesson["class"] == class_name and lesson["day"] == day and lesson["period"] == period and lesson["subject"] == subject_id):
                                first_period.append(lesson["variable"])

                            if (lesson["class"] == class_name and lesson["day"] == day and lesson["period"] == period + 1 and lesson["subject"] == subject_id):
                                next_period.append(lesson["variable"])

                        model.Add(sum(first_period) + sum(next_period) <= 1)

    solver = cp_model.CpSolver()
    for requirement in requirements:
        matching_lessons = []

        for lesson in lessons:
            if(
                lesson["class"] == requirement["className"]
                and lesson["subject"] == requirement["subjectId"]
                and lesson["teacher"] == requirement["teacherId"]
            ):
                matching_lessons.append(lesson["variable"])

        model.Add(sum(matching_lessons) >= requirement["minimumPerWeek"])
    status = solver.Solve(model)

    if status != cp_model.OPTIMAL and status != cp_model.FEASIBLE:
        raise ValueError("A timetable cant be made from these setup rules")

    schedule = {}

    for class_name in classes:
        schedule[class_name] = {}

    for lesson in lessons:
        if solver.Value(lesson["variable"]) == 1:
            slot = lesson["day"] + " P" + str(lesson["period"] + 1)

            schedule[lesson["class"]][slot] = {
                "subject": lesson["subject"],
                "teacher": lesson["teacher"]
            }

    return schedule

