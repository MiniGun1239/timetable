# --- IMPORTS ---
from flask import Flask, render_template, request, jsonify
from solver import generate_schedule
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
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send the setup as JSON"}), 400

    try:
        schedule = generate_schedule(data)
        return jsonify(schedule)

    except ValueError as error:
        return jsonify({"error": str(error)}), 400
# --- END OF HTML ROUTING ---


if __name__ == '__main__':
    run()

