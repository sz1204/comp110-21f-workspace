"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730490960"


def test_only_evens_list() -> None:
    """Tests function making sure only even numbers are in the function, from a list of odd and even numbers."""
    assert only_evens([1, 3, 4, 8, 5]) == [4, 8]


def test_only_evens_zero() -> None:
    """Tests function making sure only even numbers are in the function, when the only number is 0."""
    assert only_evens([0]) == [0]


def test_only_evens_list_evens() -> None:
    """Tests function making sure only even numbers are in the function, when the list is all even."""
    assert only_evens([10, 12, 14]) == [10, 12, 14]


def test_sub_zero() -> None:
    """Makes sure the list is a subset between two indices, when the list is 0."""
    assert sub([6, 3, 5, 2], 1, 4) == [3, 5, 2]


def test_sub_long() -> None:
    """Makes sure the list is a subset between two indices, when there is a long list."""
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]


def test_sub_all() -> None:
    """Makes sure the list is a subset between two indices, when the subset is the original list."""
    assert sub([1, 2, 3], 0, 0) == []


def test_concat_different() -> None:
    """Makes sure that two lists are concatenated into one, when there are two different lists."""
    assert concat([1, 2, 3], [4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_concat_empty() -> None:
    """Makes sure that two lists are concatenated into one, when one list is empty."""
    assert concat([0], []) == [0]


def test_concat_same() -> None:
    """Makes sure that two lists are concatenated into one, when the lists are the same."""
    assert concat([3, 4], [3, 4]) == [3, 4, 3, 4]