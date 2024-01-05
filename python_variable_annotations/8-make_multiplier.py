#!/usr/bin/env python3
""" Complex types - functions """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ Take a string & an int OR float & return float orrrr something """
    def multiplier_inception(value: float) -> float:
        return value * multiplier

    return multiplier_inception
