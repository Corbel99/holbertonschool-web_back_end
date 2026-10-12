#!/usr/bin/env python3



import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay: int) -> list:
    tasks = [wait_random(max_delay) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        delay = await tasks
        results.append(delay)

    return results
