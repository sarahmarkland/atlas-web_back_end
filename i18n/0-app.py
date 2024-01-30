#!/usr/bin/env python3
from flask import Flask, render_template
# from flask_babel import Babel

app = Flask(__name__)
# babel = Babel(app)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET / """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
