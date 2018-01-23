#!/usr/bin/env python
from flask import Flask, abort, render_template, send_file
from pathlib import Path

app = Flask(__name__)

@app.route('/last-image')
def get_image():
    all_pictures = sorted(Path('pictures').glob("*.jpg"))
    if not all_pictures:
        abort(404)
    picture = all_pictures[-1]
    return send_file(str(picture), mimetype="image/jpg", cache_timeout=-1)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8008, debug=True)