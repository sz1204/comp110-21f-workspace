"""List utility functions part 2."""

__author__ = "730490960"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    """Creates a list of integers that is composed only of even numbers."""
    evens: list[int] = list()
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            evens.append(a[i])
    return evens 


def sub(b: list[int], c: int, d: int) -> list[int]:
    """Creates a subset of a list between two indices."""
    subset: list[int] = list()

    subset = b

    if c < 0:
        c = 0
    if d > len(b):
        d = len(b) - 1
    
    i: int = 0

    if len(b) == 0:
        return b

    while i < c:
        subset.pop(b[0])
        i += 1
    
    while (len(b) - i) > (d - i):
        subset.pop(b[len(b - i) - 1])

    return subset


def concat(e: list[int], f: list[int]) -> list[int]:
    """Concatenates two lists into one."""
    new: list[int] = list()
    new = e
    i: int = 0

    while i < len(f):
        new.append(f[0])
        i += 1

    return new
