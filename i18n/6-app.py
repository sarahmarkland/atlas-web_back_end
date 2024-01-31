#!/usr/bin/env python3
""" force locale with URL parameter """
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Babel config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """ method to get user """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None
    

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 6-index.html
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """ determine best match for supported languages """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    usr = get_user()
    if usr:
        locale = usr.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
