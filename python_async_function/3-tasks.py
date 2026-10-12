#!/usr/bin/env python3
"""Create an asyncio.Task for wait_random."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The scheduled task.
    """
    return asyncio.create_task(wait_random(max_delay))
