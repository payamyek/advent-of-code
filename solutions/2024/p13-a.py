from dataclasses import dataclass
import re
from typing import List
from aocd import data


data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=1027"""


@dataclass(frozen=True)
class LinearEquation:
    x1: int
    x2: int
    b: int


@dataclass(frozen=True)
class LinearSystem:
    equations: List[LinearEquation]


def _create_linear_system() -> LinearSystem:
    for row in data.splitlines():
        if not len(row):
            continue

        if "Button" in row:
            match = re.search(r"X\+(\d+),\sY\+(\d+)", row)
            LinearEquation(match.group(1), match.group(2))


linear_system = _create_linear_system()
