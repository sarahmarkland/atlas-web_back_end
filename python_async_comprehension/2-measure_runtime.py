#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import random
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async Comprehensions """
    return [i async for i in async_generator()]


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start


async def main() -> None:
    """ Main """
    print(await measure_runtime())

if __name__ == "__main__":
    asyncio.run(main())
