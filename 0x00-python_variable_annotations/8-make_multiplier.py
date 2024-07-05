#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
