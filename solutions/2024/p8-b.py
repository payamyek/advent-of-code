from dataclasses import dataclass
from typing import List
from aocd import data, submit


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

    def __rmul__(self, other: int):
        return Point(self.x * other, self.y * other)

    def in_bounds(self, width_bounds: int, height_bounds: int) -> bool:
        return not (
            self.x < 0
            or self.x >= height_bounds
            or self.y < 0
            or self.y >= width_bounds
        )


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
            a1, a2 = antennas[frequency][i], antennas[frequency][j]

            k = 1
            while (antinode := (k * (a1 - a2) + a2)).in_bounds(GRID_WIDTH, GRID_HEIGHT):
                k += 1
                antinodes.add(antinode)

            k = 1
            while (antinode := (k * (a2 - a1) + a1)).in_bounds(GRID_WIDTH, GRID_HEIGHT):
                k += 1
                antinodes.add(antinode)


submit(len(antinodes))