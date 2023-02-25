"""Spring 2022 recursion exercise."""

from __future__ import annotations
from typing import Union


class Node:
    data: int 
    next: Union[Node, None]

    def __init__(self, data: int, next: Union[Node, None]):
        self.data = data
        self.next = next 
      
    def __str__(self) -> str:
        if self.next == None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next.__str__()}"


def sum(node: Node) -> int:
    """Returns sum of all heads"""
    if node.next is None:
        # Can also be written as if node.next == None:
        # Base case
        return node.data
    else: 
        # Recursive case
        return node.data + sum(node.next)


def count(node: Node, current_count: int = 0) -> int:
    if node.next is None:
        return 0
    else: 
        return node.data + count(node.next)

    # Can also be...
    # if node.next == None:
    #     return current_count + 1
    # else:
    #     return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))