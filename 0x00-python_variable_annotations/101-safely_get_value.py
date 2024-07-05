#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary.
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary from which to get the value.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value if the key is
        not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key, or the default value
        if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
