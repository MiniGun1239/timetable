# timetable

A school timetable generator built with - 
Python, flask, HTML, CSS and JavaScript.

Add your classes, subjects, teachers and weekly requirements, then generate a timetable. It checks teacher clashes, daily limits and no back-to-back rules.

You can view class and teacher timetables, edit cells, import/export JSON and print to PDF.

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

## AI usage

We did use ai for this project but it was just wiring up completing bad code and wiring up python with frontend. It is clearly mentioned in commit msgs when ai was used, and no other ai was used besides that.
