from dataclasses import dataclass
from typing import List
from aocd import data, submit


TRAILHEAD = 0
TRAILTAIL = 9

GRID = [list(map(int, row)) for row in data.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])


@dataclass
class Vertex:
    row: int
    col: int


TRAILHEADS = [
    Vertex(row, col)
    for row in range(GRID_HEIGHT)
    for col in range(GRID_WIDTH)
    if GRID[row][col] == TRAILHEAD
]

TRAILTAILS = [
    Vertex(row, col)
    for row in range(GRID_HEIGHT)
    for col in range(GRID_WIDTH)
    if GRID[row][col] == TRAILTAIL
]


def neighbours(v: Vertex) -> List[Vertex]:
    result = []

    # up
    if v.row > 0 and GRID[v.row - 1][v.col] - GRID[v.row][v.col] == 1:
        result.append(Vertex(v.row - 1, v.col))
    # down
    if v.row < GRID_HEIGHT - 1 and GRID[v.row + 1][v.col] - GRID[v.row][v.col] == 1:
        result.append(Vertex(v.row + 1, v.col))
    # left
    if v.col > 0 and GRID[v.row][v.col - 1] - GRID[v.row][v.col] == 1:
        result.append(Vertex(v.row, v.col - 1))
    # right
    if v.col < GRID_WIDTH - 1 and GRID[v.row][v.col + 1] - GRID[v.row][v.col] == 1:
        result.append(Vertex(v.row, v.col + 1))
    return result


def bfs(s: Vertex) -> List[List[int]]:
    queue = [s]
    discovered = [[0] * len(row) for row in GRID]

    while len(queue):
        u = queue.pop(0)
        for v in neighbours(u):
            if not discovered[v.row][v.col]:
                queue.append(v)
                discovered[v.row][v.col] = 1
    return discovered


def score(bfs_tree: List[List[int]]) -> int:
    return sum([bfs_tree[trailtail.row][trailtail.col] for trailtail in TRAILTAILS])


total = 0

for trailhead in TRAILHEADS:
    bfs_tree = bfs(trailhead)
    total += score(bfs_tree)

submit(total)
