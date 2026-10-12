#!/usr/bin/env python3
"""Define an asynchronous function that waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay=10):
    """Wait for a random delay between zero and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
