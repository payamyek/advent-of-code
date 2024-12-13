from dataclasses import dataclass
from typing import List
from aocd import data, submit


GRID = [list(row) for row in data.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])


@dataclass(frozen=True)
class Vertex:
    row: int
    col: int
    plant: str


def neighbours(v: Vertex) -> List[Vertex]:
    result = []

    # up
    if v.row > 0 and GRID[v.row - 1][v.col] == v.plant:
        result.append(Vertex(v.row - 1, v.col, v.plant))
    # down
    if v.row < GRID_HEIGHT - 1 and GRID[v.row + 1][v.col] == v.plant:
        result.append(Vertex(v.row + 1, v.col, v.plant))
    # left
    if v.col > 0 and GRID[v.row][v.col - 1] == v.plant:
        result.append(Vertex(v.row, v.col - 1, v.plant))
    # right
    if v.col < GRID_WIDTH - 1 and GRID[v.row][v.col + 1] == v.plant:
        result.append(Vertex(v.row, v.col + 1, v.plant))
    return result


def bfs(s: Vertex) -> set[Vertex]:
    queue = [s]
    discovered = set([s])

    while len(queue):
        u = queue.pop(0)
        for v in neighbours(u):
            if v not in discovered:
                queue.append(v)
                discovered.add(v)
    return discovered


def find_all_regions() -> List[set[Vertex]]:
    visited_vertices = set()
    regions: List[set[Vertex]] = []
    vertices = set(
        [
            Vertex(row, col, GRID[row][col])
            for row in range(GRID_HEIGHT)
            for col in range(GRID_WIDTH)
        ]
    )

    for vertex in vertices:
        if vertex not in visited_vertices:
            result = bfs(vertex)
            visited_vertices.update(result)
            regions.append(result)
    return regions


def fence_cost(region: set[Vertex]) -> int:
    area = len(region)
    perimeter = sum([4 - len(neighbours(vertex)) for vertex in region])
    return area * perimeter


regions = find_all_regions()

submit(sum([fence_cost(region) for region in regions]))
