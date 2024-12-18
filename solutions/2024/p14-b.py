from dataclasses import dataclass
import os
import re
from typing import List, Self
from aocd import data

WIDTH = 101
HEIGHT = 103


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

    def move(self, n: int):
        new_position = self.position + n * self.velocity
        self.position = Vector(new_position.x % WIDTH, new_position.y % HEIGHT)


def _create_robots() -> List[Robot]:
    robots: List[Robot] = []

    for row in data.splitlines():
        match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", row)
        position = Vector(int(match.group(1)), int(match.group(2)))
        velocity = Vector(int(match.group(3)), int(match.group(4)))
        robots.append(Robot(position, velocity))
    return robots


def _print_map(robots: List[Robot]):
    os.system("clear")
    result = ""
    for row in range(HEIGHT):
        for col in range(WIDTH):
            count = sum(
                [(robot.position.x, robot.position.y) == (col, row) for robot in robots]
            )
            if count:
                result += f"{count}"
                # print(f"\033[92m{count}\033[00m", end="")
            else:
                result += "."
                # print(".", end="")
        result += "\n"

    return result


robots = _create_robots()

with open("p14_b_tree.txt", "a") as f:
    for i in range(0, 300):
        for robot in robots:
            robot.move(1)

        result = _print_map(robots)
        result += f"Second {i}\n\n"
        f.write(result)
