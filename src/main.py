# --- IMPORTS ---
from flask import Flask, render_template
from pathlib import Path

# --- Class Imports ---
from objects import *
# --- End of Hitler


# --- Path Initializing stuff for stuff idk ---
DATA = Path(__file__).parent / 'data'
TEACHER_DATA = Path(__file__).parent / 'teacher.json'
SECTION_DATA = Path(__file__).parent / 'section.json'
SUBJECT_DATA = Path(__file__).parent / 'subject.json'
CONFIG = Path(__file__).parent / 'config.json'


# --- Flask Stuff ---
WEB_DIR = Path(__file__).parent.parent / 'web'
app = Flask(
    __name__,
    template_folder=WEB_DIR,
    static_folder=WEB_DIR,
    static_url_path='',
)

def run():
    app.run(debug=True)
    return
# --- END OF Flask Initializing


# --- HTML Routing stuff ---
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/generate POST')
def generate():
    pass


def test():
    section = Section(1, 11, 'B')
    teach   = Teacher(1, "Himmothy", [1], section)
    english = Subject(1, "English", [section])

    print(section.print())
    print(teach.print())
    print(english.print())


if __name__ == '__main__':
    run()

