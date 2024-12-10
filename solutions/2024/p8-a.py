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


def is_point_out_of_bounds(point: Point) -> bool:
    return point.x < 0 or point.x >= GRID_HEIGHT or point.y < 0 or point.y >= GRID_WIDTH


antennas = get_antennas()
antinodes = set()

for frequency in antennas:
    for i in range(len(antennas[frequency]) - 1):
        for j in range(i + 1, len(antennas[frequency])):
            antenna_a, antenna_b = antennas[frequency][i], antennas[frequency][j]

            first_antinode = antenna_a - antenna_b + antenna_a
            second_antinode = antenna_b - antenna_a + antenna_b

            if not is_point_out_of_bounds(first_antinode):
                antinodes.add(first_antinode)

            if not is_point_out_of_bounds(second_antinode):
                antinodes.add(second_antinode)


submit(len(antinodes))
