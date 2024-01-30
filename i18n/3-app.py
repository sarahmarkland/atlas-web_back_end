#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Babel config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ create a single route and an index.html """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def gettext():
    """ gettext function """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True, port=8080)
