#!/usr/bin/env python3
""" Module dealing with passwords """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """ Auth class to interact with the authentication database. """
    def __init__(self):
        self._db = DB()
    
    def register_user(self, email: str, password: str) -> User:
        """ Method that takes in an email string and a password string
            as arguments and returns a User object """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

def _hash_password(password: str) -> bytes:
    """ Method that takes in a string password argument and returns bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
