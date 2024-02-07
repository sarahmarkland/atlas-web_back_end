#!/usr/bin/env python3
""" writing strings to redis """
import uuid
import redis
from typing import Union
from functools import wraps


def count_calls(method):
    """ Count calls decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method):
    """ Call history decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper """
        input = f"{method.__qualname__}:inputs"
        output = f"{method.__qualname__}:outputs"
        self._redis.rpush(input, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output, str(result))
        return result
    return wrapper


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4)
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Union[None, callable] = None) -> Union[str, bytes, int, float]:
        """ Get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data


    def get_str(self, data: bytes) -> str:
        """ Get string """
        return data.decode('utf-8')


    def get_int(self, data: bytes) -> int:
        """ Get int """
        return int.from_bytes(data, byteorder='big')


def replay(method: str):
    """ Replay """
    r = redis.Redis()
    method_name = method.split('.')[1]
    count = r.get(method)
    print(f"{method_name} was called {count} times")
