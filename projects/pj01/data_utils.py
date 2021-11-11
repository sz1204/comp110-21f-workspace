"""Utility functions."""

__author__ = "730490960"


from csv import DictReader 


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selects columns that are requested to focus on them specifically."""
    result: dict[str, list[str]] = {}

    for name in names:
        result[name] = column_table.get(name, [''])

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first # rows of data for each column."""
    result: dict[str, list[str]] = {}

    if n > len(column_table):
        n = len(column_table)

    for column in column_table.keys():
        first_values = []
        for i in range(n):
            first_values.append(column_table.get(column, "")[i])
        result[column] = first_values
    
    return result


def count(values: list[str]) -> dict[str, int]:
    """Creates a dictionary where each key is a unique value in the given list, adding on how many times the value appeared in the int list."""
    result: dict[str, int] = {}

    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result


def multiple_values(list_one: list[str], list_two: list[str]) -> dict[str, int]:
    """Creates a dictionary that measures how many students who took AP are now CS majors at UNC."""
    result: dict[str, int] = {"Yes": 0, "No": 0}
    i: int = 0

    while i < len(list_one):
        if list_one[i] == "Yes":
            if list_two[i] == "No":
                result["No"] += 1
            else:
                result["Yes"] += 1
        i += 1

    return result