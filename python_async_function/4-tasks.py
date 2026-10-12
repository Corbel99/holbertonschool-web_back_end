#!/usr/bin/env python3
"""Create tasks to execute wait_random concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: The delays in the order the tasks complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
