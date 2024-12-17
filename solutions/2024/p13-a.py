from dataclasses import astuple, dataclass
import re
from typing import List
from aocd import data
from sympy import Matrix, Symbol, solve_linear_system
from sympy.abc import x, y

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
    system1: LinearEquation
    system2: LinearEquation

    def solve(self) -> dict[Symbol, int]:
        system = Matrix(astuple(self))
        return solve_linear_system(system, x, y)


def _create_linear_systems() -> List[LinearSystem]:
    systems: List[LinearSystem] = []
    coefficients: List[tuple[int, int]] = []

    for row in data.splitlines():
        if not len(row):
            continue

        if "Button" in row:
            match = re.search(r"X\+(\d+),\sY\+(\d+)", row)
            coefficients.append((match.group(1), match.group(2)))
        elif "Prize" in row:
            match = re.search(r"X=(\d+),\sY=(\d+)", row)

            x1, y1 = coefficients[0]
            x2, y2 = coefficients[1]
            b1, b2 = (match.group(1), match.group(2))

            system1 = LinearEquation(int(x1), int(x2), int(b1))
            system2 = LinearEquation(int(y1), int(y2), int(b2))

            systems.append(LinearSystem(system1, system2))

            # reset
            coefficients = []
    return systems


linear_systems = _create_linear_systems()
