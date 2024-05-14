#!/usr/bin/python3

"""
    Add Interger Task
"""

def add_integer(a, b=98):
    """
    >>> add_integer(3,6)
    9
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return a + b
