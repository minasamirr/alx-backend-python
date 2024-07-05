#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats and return their sum as a float.

    Args:
        input_list (List[float]): The list of float numbers to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
