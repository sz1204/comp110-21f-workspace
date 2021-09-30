"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730490960"


def test_only_evens() -> None:
    """Tests function making sure only even numbers are in the function."""
    assert only_evens([1, 3, 4, 8, 5])


def test_sub() -> None:
    """Makes sure the list is a subset between two indices."""
    assert sub([0], 1, 4)


def test_concat() -> None:
    """Makes sure that two lists are concatenated into one."""
    assert concat([1, 2, 3], [4, 5, 6])