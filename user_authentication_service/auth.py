#!/usr/bin/env python3
""" Module dealing with passwords """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Method that takes in an email string and a password string
            as arguments and returns a boolean """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """ Method that returns a string representation of a new UUID """
        return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """ Method that takes in a string password argument and returns bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
