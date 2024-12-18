from dataclasses import dataclass
import re
from typing import List, Self
from aocd import data

WIDTH = 11
HEIGHT = 7
SECONDS = 100

data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
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
