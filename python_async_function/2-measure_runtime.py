#!/usr/bin/env python3
"""Measure the execution time of concurrent coroutines."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time per coroutine.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Total execution time divided by n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
