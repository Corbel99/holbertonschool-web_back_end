#!/usr/bin/env python3
"""Generate random numbers asynchronously using an async generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random numbers with an asynchronous delay."""
    for i in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
