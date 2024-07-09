#!/usr/bin/env python3
"""
This module contains a function to measure the execution time of
asynchronous coroutines.

The main function, `measure_time`, measures the total execution time for the 
`wait_n` coroutine and returns the average time per coroutine.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return
    the average time per coroutine.

    Args:
        n (int): Number of coroutines.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
