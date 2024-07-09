#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension that collects random
numbers.
"""
from typing import List
async_generator = __import__('0_async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 random numbers from async_generator."""
    return [i async for i in async_generator()]
