"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float 

    def __init__(self, x: float, y: float):
        """Initializes a Point with its x, y components."""
        self.x = x 
        self.y = y 

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor 

    # def scale(self, factor: float) -> Point:
    #     """Pure method that does not mutate the Point."""
    #     """This is now unneeded due to the __mul__ method.""""
    #     # x: float = self.x * factor 
    #     # y: float = self.y * factor
    #     # p: Point = Point(x, y)
    #     # return p
    #     return Point(self.x * factor, self.y * factor)
    #     # Using argument expressions directly rather than splitting up into multiple steps

    def __str__(self) -> str:
        """Magic method that produces a str representation of a Point for humans."""
        # print("__str__ was called!")
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Magic method that produces a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Overload the addition operator for Point + Point where rhs is right hand side."""
        return Point(self.x + rhs.x, self.y + rhs.y)
    
    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y 
        else: 
            raise IndexError
    

p0: Point = Point(1.0, 2.0)
p1: Point = p0 * 2.0
p2: Point = p0 + p1
print(f"p2: {p2}")

print(p0[0])
print(p0[1])

# p1: Point = p0.scale(2.0)
print(p0)
# Technically print(p0.__str__()), but is automatically happening for us so no need to call the method.

p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)