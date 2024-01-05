#!/usr/bin/env python3

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Write a function (do not create an async function,
        use the regular function syntax to do this) task_wait_n
        that takes an integer n and max_delay and returns a list
        of all the delays (float values)."""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
