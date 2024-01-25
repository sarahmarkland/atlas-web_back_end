#!/usr/bin/env python3
"""
basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from flask.helpers import make_response
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"})
