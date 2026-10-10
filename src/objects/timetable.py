from dataclasses import dataclass, asdict, field
from ortools.sat.python import cp_model

from objects import config, Section, Subject, Teacher

Config = config.Config


@dataclass
class Timetable:
    section: int
    rows: dict[str, list[int | None]]

    _instances: list = field(
        default_factory=list,
        init=False,
        repr=False
    )

    def __repr__(self) -> str:
        section_name = self.section

        for section in Section.getInstances():
            if section.id == self.section:
                section_name = section.get()
                break

        output = f"Timetable for {section_name}:\n"
        for day, row in self.rows.items():
            output += f"  {day}: {row}\n"
        return output

    def __post_init__(self):
        self._instances.append(self)

    def addRow(self, row: dict[str, list[int | None]]) -> bool:
        self.rows.update(row)
        return True

    def serialize(self):
        return asdict(self)

    @classmethod
    def deserialize(cls, data: dict) -> "Timetable":
        return cls(
            data["section"],
            data["rows"],
        )


def create(config: Config) -> list[Timetable]:
    model = cp_model.CpModel()

    days = config.days  # [cite: 1]
    periods_count = config.periods  # [cite: 1]

    # Handle both list or dict configurations safely
    teachers = list(config.teachers.values()) if isinstance(config.teachers, dict) else config.teachers  # [cite: 1]
    sections = list(config.sections.values()) if isinstance(config.sections, dict) else config.sections  # [cite: 1]
    subjects = list(config.subjects.values()) if isinstance(config.subjects, dict) else config.subjects  # [cite: 1]

    # Helper to handle whether items are dataclass instances or dictionaries
    def get_attr(obj, attr, default=None):
        if isinstance(obj, dict):
            return obj.get(attr, default)
        return getattr(obj, attr, default)

    sub_map = {get_attr(s, 'id'): s for s in subjects}
    teach_list = list(teachers)
    sec_list = list(sections)

    # Decision variables:
    # x[sec_id, day, period, sub_id, teach_id] = 1 if active else 0
    x = {}

    for sec in sec_list:
        sec_id = get_attr(sec, 'id')
        sec_subjects = get_attr(sec, 'subjects', [])  # [cite: 2]

        for d in days:
            for p in range(periods_count):
                for sub_id in sec_subjects:
                    valid_teachers = [
                        t for t in teach_list
                        if sub_id in get_attr(t, 'subjects', [])  # [cite: 4]
                    ]
                    for t in valid_teachers:
                        t_id = get_attr(t, 'id')
                        x[(sec_id, d, p, sub_id, t_id)] = model.NewBoolVar(
                            f"sec_{sec_id}_{d}_p{p}_sub_{sub_id}_t_{t_id}"
                        )

    # Constraint 1: Exactly one subject & teacher per section per period
    for sec in sec_list:
        sec_id = get_attr(sec, 'id')
        sec_subjects = get_attr(sec, 'subjects', [])  # [cite: 2]

        for d in days:
            for p in range(periods_count):
                period_vars = []
                for sub_id in sec_subjects:
                    valid_teachers = [
                        t for t in teach_list
                        if sub_id in get_attr(t, 'subjects', [])  # [cite: 4]
                    ]
                    for t in valid_teachers:
                        t_id = get_attr(t, 'id')
                        if (sec_id, d, p, sub_id, t_id) in x:
                            period_vars.append(x[(sec_id, d, p, sub_id, t_id)])
                if period_vars:
                    model.Add(sum(period_vars) == 1)

    # Constraint 2: Subject frequency per week per section
    for sec in sec_list:
        sec_id = get_attr(sec, 'id')
        sec_subjects = get_attr(sec, 'subjects', [])  # [cite: 2]

        for sub_id in sec_subjects:
            sub_obj = sub_map.get(sub_id)
            target_count = get_attr(sub_obj, 'times_per_week', 1)  # [cite: 3]

            sub_vars = []
            for d in days:
                for p in range(periods_count):
                    valid_teachers = [
                        t for t in teach_list
                        if sub_id in get_attr(t, 'subjects', [])  # [cite: 4]
                    ]
                    for t in valid_teachers:
                        t_id = get_attr(t, 'id')
                        if (sec_id, d, p, sub_id, t_id) in x:
                            sub_vars.append(x[(sec_id, d, p, sub_id, t_id)])
            if sub_vars:
                model.Add(sum(sub_vars) == target_count)

    # Constraint 3: Teacher conflict — a teacher cannot be in two sections at the same time
    for t in teach_list:
        t_id = get_attr(t, 'id')
        t_subjects = get_attr(t, 'subjects', [])  # [cite: 4]

        for d in days:
            for p in range(periods_count):
                teacher_period_vars = []
                for sec in sec_list:
                    sec_id = get_attr(sec, 'id')
                    sec_subjects = get_attr(sec, 'subjects', [])  # [cite: 2]
                    for sub_id in sec_subjects:
                        if sub_id in t_subjects:
                            if (sec_id, d, p, sub_id, t_id) in x:
                                teacher_period_vars.append(x[(sec_id, d, p, sub_id, t_id)])
                if teacher_period_vars:
                    model.Add(sum(teacher_period_vars) <= 1)

        # Constraint 4: Back-to-back Policies (FORCE / FORBID)
        for sec in sec_list:
            sec_id = get_attr(sec, 'id')
            sec_subjects = get_attr(sec, 'subjects', [])  # [cite: 2]

            for sub_id in sec_subjects:
                sub_obj = sub_map.get(sub_id)
                policy = get_attr(sub_obj, 'back2back')

                if not policy:
                    continue

                # Convert enum or string value safely
                policy_val = policy.value if hasattr(policy, 'value') else policy

                if policy_val == "FORBID":
                    # Forbid same subject in consecutive periods on the same day
                    for d in days:
                        for p in range(periods_count - 1):
                            # Find all teacher variables for period p and period p+1
                            p_vars = [
                                x[(sec_id, d, p, sub_id, get_attr(t, 'id'))]
                                for t in teach_list
                                if sub_id in get_attr(t, 'subjects', [])  # [cite: 4]
                                   and (sec_id, d, p, sub_id, get_attr(t, 'id')) in x
                            ]
                            p_next_vars = [
                                x[(sec_id, d, p + 1, sub_id, get_attr(t, 'id'))]
                                for t in teach_list
                                if sub_id in get_attr(t, 'subjects', [])  # [cite: 4]
                                   and (sec_id, d, p + 1, sub_id, get_attr(t, 'id')) in x
                            ]
                            if p_vars and p_next_vars:
                                # They cannot BOTH be 1
                                model.Add(sum(p_vars) + sum(p_next_vars) <= 1)

                elif policy_val == "FORCE":
                    for d in days:
                        # Helper function to sum all teacher variables for a subject at a specific day and period
                        def get_period_sum(p_idx):
                            return sum(
                                x[(sec_id, d, p_idx, sub_id, get_attr(t, 'id'))]
                                for t in teach_list
                                if sub_id in get_attr(t, 'subjects', [])  # [cite: 4]
                                and (sec_id, d, p_idx, sub_id, get_attr(t, 'id')) in x
                            )

                        last_p = periods_count - 1
                        for p in range(periods_count):
                            p_sum = get_period_sum(p)
                            if p == 0:
                                # If it's at the very start, it must be followed by period 1
                                next_sum = get_period_sum(1)
                                model.Add(p_sum <= next_sum)
                            elif p == last_p:
                                # If it's at the very end, it must be preceded by the second-to-last period
                                prev_sum = get_period_sum(last_p - 1)
                                model.Add(p_sum <= prev_sum)
                            else:
                                # For any middle period, it needs at least one neighbor (before or after)
                                prev_sum = get_period_sum(p - 1)
                                next_sum = get_period_sum(p + 1)
                                model.Add(p_sum <= prev_sum + next_sum)

    # Solve the model
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 30.0
    status = solver.Solve(model)

    timetables = []

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for sec in sec_list:
            sec_id = get_attr(sec, 'id')
            rows = {}
            for d in days:
                day_periods = []
                for p in range(periods_count):
                    assigned_sub = None
                    sec_subjects = get_attr(sec, 'subjects', [])  # [cite: 2]
                    for sub_id in sec_subjects:
                        valid_teachers = [
                            t for t in teach_list
                            if sub_id in get_attr(t, 'subjects', [])  # [cite: 4]
                        ]
                        for t in valid_teachers:
                            t_id = get_attr(t, 'id')
                            key = (sec_id, d, p, sub_id, t_id)
                            if key in x and solver.Value(x[key]) == 1:
                                assigned_sub = sub_id
                                break
                        if assigned_sub is not None:
                            break
                    day_periods.append(assigned_sub)
                rows[d] = day_periods

            timetables.append(Timetable(section=sec_id, rows=rows))
    else:
        print("No feasible timetable found!")

    return timetables


if __name__ == "__main__":
    configuration = config.sample()

    timetables = create(configuration)
    for tt in timetables:
        print(tt)

