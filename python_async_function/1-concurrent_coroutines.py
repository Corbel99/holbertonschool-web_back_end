#!/usr/bin/env python3
"""
Une coroutine qui lance wait_n fois wait_random avec un délai maximum donné
et retourne la liste des délais par ordre croissant.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
  """Lance wait_random n fois avec max_delay

  et retourne la liste de tous les délais par ordre croissant.
  """
  tasks = [wait_random(max_delay) for _ in range(n)]
  results = []

  for task in asyncio.as_completed(tasks):
    delay = await task
    results.append(delay)

  return results
