#!/usr/bin/env python3
""" writing strings to redis """
import redis


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """ Store data in redis """
        key = self._redis.get('key')
        self._redis.set('key', data)
        return key
