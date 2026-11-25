# timetable

Timetable generator built with Flask.

## Features

- Generate timetables from your school setup
- Set teacher limits and minimum lessons per week
- Avoid teacher clashes and back-to-back subjects
- View timetables by class or teacher
- View free teachers
- Edit timetable cells
- Import and export JSON
- Print or save as PDF

## Stack

- Python
- Flask
- OR-Tools
- HTML
- CSS
- JavaScript


## Run it

Install Python 3.12+ and [uv](https://docs.astral.sh/uv/), then:

```sh
git clone https://github.com/MiniGun1239/timetable.git
cd timetable
uv sync
uv run python src/main.py
```

Open http://localhost:5000.

Fill in the setup and add weekly requirements for each class. Click Generate to see the result.

## screenshots

<img width="1858" height="973" alt="image" src="https://github.com/user-attachments/assets/5a8b30f4-0771-45c1-943a-aa588c2d3d5d" />
<img width="1858" height="973" alt="image" src="https://github.com/user-attachments/assets/785260ca-6bbe-469f-bd51-6910f4af7607" />

## Example setup

```text
School: fish
Days: Monday to Friday
Periods per day: 4
Period length: 40 minutes
Grade: 10
Section: A

Subjects:
Maths
English
Leave "No back to back" unchecked for both.

Teachers:
Alex: Maths, max 4 periods per day
Sam: English, max 4 periods per day

Weekly requirements:
Maths | 10-A | Alex | Minimum 10
English | 10-A | Sam | Minimum 10
```

Click Generate. This gives you 20 periods: 10 Maths and 10 English.

## AI usage

We did use ai for this project but it was just wiring up completing bad code and wiring up python with frontend. It is clearly mentioned in commit msgs when ai was used, and no other ai was used besides that.
