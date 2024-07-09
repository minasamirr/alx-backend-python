#!/usr/bin/env python3
"""
This module contains a function to create an asyncio.Task for the wait_random
coroutine.

The main function, `task_wait_random`, creates an asyncio.Task for the
wait_random coroutine with a specified maximum delay.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine with the specified
    max_delay.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The created asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
