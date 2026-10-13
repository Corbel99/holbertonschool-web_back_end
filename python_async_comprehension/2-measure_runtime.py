#!/usr/init/env python3
"""Measure the runtime of async_comprehension executed four times in parallel."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times using asyncio.gather and measure the total runtime."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    total_time = end - start
    return total_time
