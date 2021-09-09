"""Drawing forests in a loop."""

__author__ = "730490960"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

ask: int = int(input("Depth: "))
i: int = 1
k: int = 1
add: str = ""

while i <= ask:

    while i >= k:
        add = add + TREE
        k = k + 1

    i = i + 1
    print(add)