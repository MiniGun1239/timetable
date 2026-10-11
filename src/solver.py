from ortools.sat.python import cp_model

# idrk, this might be bad code
# i dont usually write python, actually never

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
            class_name = requirement.get("class_name")
            subject_id = requirement.get("subjectId")
            teacher_id = requirement.get("teacherId")
            minimum = requirement.get("minimumPerWeek")

        if class_name not in classes:
            raise ValueError("Weekly requirement has an unknow class")