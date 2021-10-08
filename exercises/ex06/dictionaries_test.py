"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730490960"


def test_invert_long() -> None:
    """Assures that a longer list composed of letters is inverted properly."""
    assert invert({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}) == ({'b': 'a', 'd': 'c', 'f': 'e', 'h': 'g'})


def test_invert_short() -> None:
    """Assures that a short list composed of words is inverted properly."""
    assert invert({"hello": "bye", "thank you": "you're welcome"}) == ({"bye": "hello", "you're welcome": "thank you"})


def test_invert_keyerror() -> None:
    """Creates a dictionary that will guarantee a KeyError."""
    assert invert({"tortilla": "chips", "lays": "chips"})


def test_favorite_color_basic() -> None:
    """Basic test of favorite_color definition that has a popular favorite color."""
    assert favorite_color({"Maya": "blue", "Sarah": "green", "Marisa": "green", "Dan": "green", "Felix": "red"}) == "green"


def test_favorite_color_first() -> None:
    """Test in which there is no favorite color, so the first color is returned."""
    assert favorite_color({"Sarah": "brown", "Bela": "green", "Carina": "white"}) == "brown"


def test_favorite_color_tie() -> None:
    """Test in where there is a tie for favorite color."""
    assert favorite_color({"Hailey": "red", "Molly": "yellow", "Chico": "red", "Chloe": "yellow"}) == "red"


def test_count_nums() -> None:
    """Test in which a generic list of numbers is tested."""
    assert count(["1", "1", "2", "3"]) == ({"1": 2, "2": 1, "3": 1})


def test_count_word() -> None:
    """Test in which a word is tested."""
    assert count(["h", "a", "p", "p", "y"]) == ({"h": 1, "a": 1, "p": 2, "y": 1})


def test_count_edge() -> None:
    """Edge case for count test in which there are no values."""
    assert count([]) == ({})