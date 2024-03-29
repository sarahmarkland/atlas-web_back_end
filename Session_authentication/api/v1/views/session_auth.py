#!/usr/bin/env python3
"""
VIEWS version
Create a new Flask view that handles all routes for the Session authentication
"""
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.auth import Auth

auth = None
if getenv('AUTH_TYPE') == 'session_auth':
    auth = SessionAuth()
else:
    auth = Auth()


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})
    if user == []:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    user_dict = jsonify(user[0].to_json())
    user_dict.set_cookie(getenv('SESSION_NAME'), session_id)
    return user_dict
