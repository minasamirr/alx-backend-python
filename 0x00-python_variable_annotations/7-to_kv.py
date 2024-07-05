#!/usr/bin/env python3
"""
This module provides a function to create a tuple with a string and the square of a number.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the number.
    """
    return (k, float(v ** 2))
