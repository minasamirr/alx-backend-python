#!/usr/bin/env python3
"""
This module contains a coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""
import asyncio
import time
from importlib import import_module as using
async_comprehension = using('1_async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of running async_comprehension four times
    in parallel."""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
