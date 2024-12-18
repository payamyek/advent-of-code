from dataclasses import dataclass
import re
from typing import List, Self
from aocd import data

WIDTH = 11
HEIGHT = 7
SECONDS = 5

data = """p=2,4 v=2,-3
"""


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __rmul__(self, other: int) -> Self:
        if not isinstance(other, int):
            raise Exception("Vector only supports scalar multiplication.")
        return Vector(self.x * other, self.y * other)


@dataclass
class Robot:
    position: Vector
    velocity: Vector

    def move(self):
        new_position = self.position + SECONDS * self.velocity
        self.position = Vector(new_position.x % WIDTH, new_position.y % HEIGHT)


def _create_robots() -> List[Robot]:
    robots: List[Robot] = []

    for row in data.splitlines():
        match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", row)
        position = Vector(int(match.group(1)), int(match.group(2)))
        velocity = Vector(int(match.group(3)), int(match.group(4)))
        robots.append(Robot(position, velocity))
    return robots


robots = _create_robots()

for robot in robots:
    robot.move()

print(*robots, sep="\n")
