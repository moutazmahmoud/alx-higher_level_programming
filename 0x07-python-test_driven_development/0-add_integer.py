#!/usr/bin/python3
"""
    Adds two integers.

    Parameters:
    a (int, float): The first number to add.
    b (int, float, optional): The second number to add. Defaults to 98.

    Returns:
    int: The sum of a and b, casted to integers if they are floats.

    Raises:
    TypeError: If a or b are not integers or floats.
"""

def add_integer(a, b=98):
    """
    >>> add_integer(3,6)
    9
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
