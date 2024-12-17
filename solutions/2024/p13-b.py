from dataclasses import astuple, dataclass
import re
from typing import List
from aocd import data, submit
from sympy import Matrix, Symbol, solve_linear_system
from sympy.abc import x, y


OFFSET = 10000000000000


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

            system1 = LinearEquation(int(x1), int(x2), int(b1) + OFFSET)
            system2 = LinearEquation(int(y1), int(y2), int(b2) + OFFSET)

            systems.append(LinearSystem(system1, system2))

            # reset
            coefficients = []
    return systems


def _required_tokens(result: dict[Symbol, int]) -> int:
    if not len(result) or not result[x].is_integer or not result[y].is_integer:
        return 0
    return int(3 * result[x] + result[y])


linear_systems = _create_linear_systems()

tokens = sum([_required_tokens(system.solve()) for system in linear_systems])

submit(tokens)
