# --- IMPORTS ---
from flask import Flask, render_template
from constants import *
# --- End of IMPORTS


# --- Flask Stuff ---
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


# --- HTML ROUTING stuff ---
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/generate', methods=['POST'])
def generate():
    pass
# --- END OF HTML ROUTING ---


if __name__ == '__main__':
    run()

