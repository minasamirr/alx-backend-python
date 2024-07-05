#!/usr/bin/env python3
"""
This module provides a function to zoom in on an array by repeating its
elements.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on an array by repeating its elements.

    Args:
        lst (Tuple[int, ...]): The tuple of integers to zoom in on.
        factor (int, optional): The factor by which to repeat each element.
        Defaults to 2.

    Returns:
        List[int]: The zoomed-in array as a list of integers.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
