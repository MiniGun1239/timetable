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


@app.route('POST /api/generate')
def generate():
    pass


def main():
    pass


if __name__ == '__main__':
    app.run()
    main()

