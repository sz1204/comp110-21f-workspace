"""List utility functions part 2."""

__author__ = "730490960"


def only_evens(a: list[int]) -> list[int]:
    """Creates a list of integers that is composed only of even numbers."""
    evens: list[int] = list()
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            evens.append(a[i])
        i += 1
    return evens 


def sub(b: list[int], c: int, d: int) -> list[int]:
    """Creates a subset of a list between two indices."""
    subset: list[int] = list()
    if c < 0:
        c = 0
    if d > len(b):
        d = len(b)
    if len(b) == 0 or c > len(b) or d <= 0:
        return subset
    i: int = c
    while i < d:
        subset.append(b[i])
        i += 1
    return subset


def concat(e: list[int], f: list[int]) -> list[int]:
    """Concatenates two lists into one."""
    new: list[int] = list()
    new = e
    i: int = 0
    while i < len(f):
        new.append(f[i])
        i += 1
    return new
