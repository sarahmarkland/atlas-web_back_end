#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@app.route('/')
def index():
    return render_template('index.html', title='Welcome to Holberton',\
                           header='Hello world')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
