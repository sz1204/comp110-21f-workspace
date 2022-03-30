"""Practice with dictionaries."""

__author__ = "730490960"


def invert(orig: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and the values."""
    inverted: dict[str, str] = {}
    for letter in orig:
        if orig[letter] in inverted:
            raise KeyError("This value has already been used as a key.")
        inverted[orig[letter]] == letter
    return inverted


def favorite_color(table: dict[str, str]) -> str:
    """Returns which color is the most popular from a dictionary."""
    color_to_count: dict[str, int] = {}
    for name in table:
        color: str = table[name]
        if color in color_to_count:
            color_to_count[color] += 1
        else:
            color_to_count[color] = 1
    max_count: int = 0
    max_color: str = ""
    for color in color_to_count:
        count: int = color_to_count[color]
        if count > max_count:
            max_count = count
            max_color = color
    return max_color


def count(times: list[str]) -> dict[str, int]:
    """Puts a list of integer values into a dictionary."""
    recount = dict[str, int]
    recount = dict()
    for number in times:
        if number in recount:
            recount[number] += 1
        else:
            recount[number] = 1
    return recount