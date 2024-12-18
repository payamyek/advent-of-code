from dataclasses import dataclass
import re
from typing import List, Self
from aocd import data, submit

WIDTH = 101
HEIGHT = 103
SECONDS = 100

# split horizontally
# split vertically

Q1_X, Q1_Y = (0, WIDTH // 2), (0, HEIGHT // 2)
Q2_X, Q2_Y = (WIDTH - WIDTH // 2, WIDTH), (0, HEIGHT // 2)
Q3_X, Q3_Y = (0, WIDTH // 2), (HEIGHT - HEIGHT // 2, HEIGHT)
Q4_X, Q4_Y = (WIDTH - WIDTH // 2, WIDTH), (HEIGHT - HEIGHT // 2, HEIGHT)


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


def _num_of_robots_in_quadrant(
    robots: List[Robot], x_bounds: tuple[int, int], y_bounds: tuple[int, int]
) -> int:
    total = 0

    x_min, x_max = x_bounds
    y_min, y_max = y_bounds

    for robot in robots:
        if (
            robot.position.x >= x_min
            and robot.position.x < x_max
            and robot.position.y >= y_min
            and robot.position.y < y_max
        ):
            total += 1
    return total


robots = _create_robots()

for robot in robots:
    robot.move()

total = (
    _num_of_robots_in_quadrant(robots, Q1_X, Q1_Y)
    * _num_of_robots_in_quadrant(robots, Q2_X, Q2_Y)
    * _num_of_robots_in_quadrant(robots, Q3_X, Q3_Y)
    * _num_of_robots_in_quadrant(robots, Q4_X, Q4_Y)
)


submit(total)
