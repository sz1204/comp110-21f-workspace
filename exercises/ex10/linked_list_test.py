"""Tests for linked list utils."""

from __future__ import annotations
from exercises.ex10.linked_list import Node, last, is_equal, value_at, max, linkify, scale
import pytest

__author__ = "730490960"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value at of an index that doesn't exist should raise an Index error."""
    with pytest.raises(IndexError):
        value_at(None, 3)


def test_value_at_regular() -> None:
    """Regular test case of value_at."""
    linked_list = (Node(10, Node(20, Node(30, None))))
    assert value_at(linked_list, 0) == 10


def test_max_empty() -> None:
    """Max of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        max(None)


def test_max_regular() -> None:
    """Regular test case of max"""
    linked_list = (Node(10, Node(20, Node(30, None))))
    assert max(linked_list) == 30


def test_linkify_empty() -> None:
    """Linkify of an empty list should return none."""
    assert linkify([]) is None


def test_linkify_regular() -> None:
    """Regular test case for linkify."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(linkify([1, 2, 3]), linked_list)
    

def test_scale_empty() -> None:
    """Scale of an empty list should return none."""
    assert scale(None, 2) is None


def test_scale_non_empty() -> None:
    """Scale of an list should return a linked list with values multiplied by a factor."""
    assert is_equal(scale(Node(1, Node(2, Node(3, None))), 2), Node(2, Node(4, Node(6, None))))
