#!/usr/bin/env python3

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        )
    end = time.perf_counter()
    total_time = end - start
    return total_time
