from dataclasses import dataclass
from typing import List
from aocd import data


GRID = [list(row) for row in data.splitlines()]
GRID_WIDTH = len(GRID[0])
GRID_HEIGHT = len(GRID)


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __sub__(self, other):
        return Point((self.x - other.x), (self.y - other.y))

    def __add__(self, other) -> tuple[int, int]:
        return Point((self.x + other.x), (self.y + other.y))
    
    def in_bounds(self, width_bounds: int, height_bounds: int)-> bool:
        return self.x < 0 or self.x >= height_bounds or self.y < 0 or self.y >= width_bounds


def is_antenna(input: str):
    return input.isalnum()


def get_antennas() -> dict[str, List[Point]]:
    antennas = dict()
    for row in range(len(GRID)):
        for col in range(len(GRID[row])):
            if not is_antenna(GRID[row][col]):
                continue

            antenna = GRID[row][col]
            if antennas.get(antenna) is None:
                antennas[antenna] = [Point(row, col)]
            else:
                antennas[antenna].append(Point(row, col))
    return antennas


antennas = get_antennas()
antinodes = set()

for frequency in antennas:
    for i in range(len(antennas[frequency]) - 1):
        for j in range(i + 1, len(antennas[frequency])):
            antenna_a, antenna_b = antennas[frequency][i], antennas[frequency][j]


print(len(antinodes))
