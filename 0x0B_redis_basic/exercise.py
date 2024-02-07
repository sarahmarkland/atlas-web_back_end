#!/usr/bin/env python3
""" writing strings to redis """
import uuid
import redis
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
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


def replay(method: Callable) -> None:
    """ Replay decorator """
    name = method.__qualname__
    input = f"{name}:inputs"
    output = f"{name}:outputs"
    print(f"{name} was called {method.__self__._redis.get(name)} times:")
    inputs = method.__self__._redis.lrange(input, 0, -1)
    outputs = method.__self__._redis.lrange(output, 0, -1)
    for i, o in zip(inputs, outputs):
        print(f"{name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")
