import os

from flask import Flask, render_template, request


UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit-cv', methods=['POST'])
def submit_cv():
    if 'cv' not in request.files:
        return 'No file part', 400

    file = request.files['cv']

    if not file or file.filename == '':
        return 'No selected file', 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return render_template('upload_success.html', filename=file.filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
