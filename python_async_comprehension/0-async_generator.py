#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main() -> None:
    """ Main """
    async for i in async_generator():
        print(i)


if __name__ == "__main__":
    asyncio.run(main())
