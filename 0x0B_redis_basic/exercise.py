#!/usr/bin/env python3
""" writing strings to redis """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        self._redis.set('key', data)
        return data
