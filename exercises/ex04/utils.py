"""List utility functions."""

__author__ = "730490960"


# TODO: Implement your functions here.


def all(haystack: list[int], needle: int) -> bool:
    """Returns true if all numbers in haystack match the indicated needle."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] != needle:
            return False
        i += 1
    return True


def is_equal(one: list[int], two: list[int]) -> bool:
    """Compares two lists of int values and returns True if each element at every index is equal."""
    i: int = 0
    if len(one) == len(two):
        while i < len(one):
            if one[i] != two[i]:
                return False
            i += 1
    else:
        return False
    return True


def max(largest: list[int]) -> int:
    if len(largest) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = 0
    while i < len(largest):
        if largest[i] > max:
            max = largest[i]
    return max