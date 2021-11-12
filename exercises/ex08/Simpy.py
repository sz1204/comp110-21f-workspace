"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730490960"


class Simpy:
    """A class that is helpful for working with sequences of numerical data."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes a new values attribute of the Simpy class."""
        self.values = values

    def __str__(self) -> str:
        """Converts the Simpy object to a str representation."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """The fill method fills the values array by mutating the object it is called on."""
        self.values = []
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with a range of values that are floats."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step 
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step 
            
    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for exponentiation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compares two Simpy values or a Simpy and a float value to see if they are equal."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            i: int = 0
            while i < len(self.values):
                if self.values[i] != rhs.values[i]:
                    result.append(False)
                else:
                    result.append(True)
                i += 1
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compares two Simpy objects or a Simpy and a float to see if the values are greater than the values in another list."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription notation support of objects in the Simpy class."""
        if isinstance(rhs, int):
            value: float = 0.0
            value = self.values[rhs]
            return value
        else:
            result: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self.values[i])
            return result