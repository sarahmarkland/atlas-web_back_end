#!/usr/bin/env python3
""" Module dealing with passwords """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Method that takes in a string password argument and returns bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
