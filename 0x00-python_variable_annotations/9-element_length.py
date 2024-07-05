#!/usr/bin/env python3
"""
This module provides a function to get the length of elements in an iterable.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get the length of elements in an iterable.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with sequences and their
        lengths.
    """
    return [(i, len(i)) for i in lst]
