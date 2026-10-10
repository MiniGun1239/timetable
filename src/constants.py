from pathlib import Path

# --- Path Initializing stuff for stuff idk ---
DATA = Path(__file__).parent / 'data'

TEACHER_DATA = DATA / 'teachers.json'
SECTION_DATA = DATA / 'sections.json'
SUBJECT_DATA = DATA / 'subjects.json'
CONFIG_DATA  = DATA / 'config.json'
TIMETABLE_DATA = DATA / 'timetables.json'

WEB_DIR = Path(__file__).parent.parent / 'web'
# --- Path initializing done ig

