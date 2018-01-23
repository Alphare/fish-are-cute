#!/usr/bin/env python
from flask import Flask, abort, render_template, send_file
from pathlib import Path

app = Flask(__name__)

@app.route('/last-image')
def get_image():
    all_pictures = Path('pictures').glob("*.jpg")
    picture = None
    for _ in sorted(all_pictures):
        picture = _
    if not picture:
        abort(404)
    return send_file(str(picture), mimetype="image/jpg", cache_timeout=-1)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8008, debug=True)