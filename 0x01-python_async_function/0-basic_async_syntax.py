#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.

The main coroutine, `wait_random`, waits for a random delay between 0 and a
specified maximum number of seconds and then returns the actual delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
