#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ Take a string & an int OR float & return float orrrr something """
    theTuple = (k, float(v) ** 2)
    return (theTuple)
