"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt

# from __future__ import annotations
# from random import random
# import constants
# from math import sin, cos, pi, sqrt


__author__ = "730399208"  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns the distance between two point objects."""
        distance: float = sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Keeps track of time in simulation."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
            if self.sickness >= constants.RECOVERY_PERIOD:
                self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected():
            return "red"
        elif self.is_immune():
            return "pink"
        return "gray"

    def contract_disease(self) -> None:
        """Makes cell infected."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Returns True if cell is vulnerable, false otherwise."""
        return (self.sickness == constants.VULNERABLE)
    
    def is_infected(self) -> bool:
        """Returns True if cell is infected, false otherwise."""
        return (self.sickness >= constants.INFECTED)
    
    def contact_with(self, other: Cell) -> None:
        """Makes proper adjustments when two cells come into contact with one another."""
        if (self.is_infected() and other.is_vulnerable()):
            other.contract_disease()
        elif (self.is_vulnerable() and other.is_infected()):
            self.contract_disease()
    
    def immunize(self) -> None:
        """Assigns immune to sickness attribute."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Returns True if the cell is immune, false otherwise."""
        return (self.sickness == constants.IMMUNE)


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_cells >= cells or infected_cells <= 0:
            raise ValueError("Infected cells cannot be <=0 and cannot be greater than total num of cells.")
        if immune_cells >= cells or immune_cells < 0:
            raise ValueError("Immune cells cannot be greater than total cells or <0.")
        self.population = []
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)f
            if i in range(infected_cells):
                self.population[i].contract_disease()
            if i in range(infected_cells, infected_cells + immune_cells):
                self.population[i].immunize()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in range(0, len(self.population)):
            if self.population[i].is_infected():
                return False
        return True
    
    def check_contacts(self) -> None:
        """Checks whether any two cells have come into contact with one another."""
        for i in range(0, len(self.population)):
            for j in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])