#!/usr/bin/env python3
""" Complex types - mixed list """
import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """ Take a mixed list of ints & floats and return float """
    return sum(mxd_list)
