#!/usr/bin/env python3
'''Execute multiple coroutines at the same time with async'''
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    '''takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values)
    in ascending order without using sort() because of concurrency.'''
    delays = []
    for i in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(delays)]
