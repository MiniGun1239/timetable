from flask import Flask, render_template


from objects import *


app = Flask(
    __name__,
    template_folder='../web',
    static_folder='../web',
    static_url_path='',
)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/generate POST')
def generate():
    pass


def run():
    app.run(debug=True)
    return


def main():
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

