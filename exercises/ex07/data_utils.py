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


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first # rows of data for each column."""
    # Establishing an empty dict that will be returned
    result: dict[str, list[str]] = {}
    # If the user enters a number greater than how many columns are in the table, set it equal to the length of the column.
    if n > len(column_table):
        n = len(column_table)

    for column in column_table.keys():
        first_values = []
        for i in range(n):
            first_values.append(column_table.get(column, "")[i])
        result[column] = first_values
    return result


# def head(table: dict[str, list[str]], count: int) -> dict[str, list[str]]:
#     """Shows the first few rows of data for each column."""
#     result: dict[str, list[str]] = {}

#     for column in table:
#         values: list[str] = []
#         for value in table[column]:
#             if len(values) < count:
#                 values.append(value)
#         result[column] = values
#     return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selects columns that are requested to focus on them specifically."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = column_table.get(name, [''])
    return result


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines tables of data to perform easier analysis."""
    result: dict[str, list[str]] = {}
    for x in dict1.keys():
        result[x] = dict1.get(x, [''])
    for y in dict2.keys():
        if y in result.keys():
            exist = result.get(y)
            exist += dict2.get(y)
            result[y] = exist
        else:
            result[y] = dict2.get(y, [''])
    return result

# def concat(firsttable: dict[str, list[str]], secondtable: dict[str, list[str]]) -> dict[str, list[str]]:
#     """Produces a new table comprised of two combined tables."""
#     result: dict[str, list[str]] = {}

#     for column in firsttable:
#         result[column] = firsttable[column]
#     for column in secondtable:
#         if column in result:
#             result[column] += secondtable[column]
#         else:
#             result[column] = secondtable[column]
#     return result


def count(values: list[str]) -> dict[str, int]:
    """Creates a dictionary where each key is a unique value in the given list, adding on how many times the value appeared in the int list."""
    result: dict[str, int] = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result