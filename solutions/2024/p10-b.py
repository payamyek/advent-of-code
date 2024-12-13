from dataclasses import dataclass, field
from enum import Enum
from typing import List, Self, Union
from aocd import data, submit


TRAILHEAD = 0
TRAILTAIL = 9

GRID = [list(map(int, row)) for row in data.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])


class VertexColour(Enum):
    WHITE = 0  # not discovered
    GREY = 1  # discovered
    BLACK = 2  # finished exploring


@dataclass
class Vertex:
    row: int
    col: int
    colour: Enum = field(compare=False, default=VertexColour.WHITE)
    predecessor: Union[Self, None] = field(compare=False, default=None, repr=False)
    paths: int = field(compare=False, default=1)


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


def neighbours(v: Vertex, vertices=List[Vertex]) -> List[Vertex]:
    result = []

    # up
    if v.row > 0 and GRID[v.row - 1][v.col] - GRID[v.row][v.col] == 1:
        result.append(
            next(
                (
                    vertex
                    for vertex in vertices
                    if (v.row - 1, v.col) == (vertex.row, vertex.col)
                ),
                None,
            )
        )
    # down
    if v.row < GRID_HEIGHT - 1 and GRID[v.row + 1][v.col] - GRID[v.row][v.col] == 1:
        result.append(
            next(
                (
                    vertex
                    for vertex in vertices
                    if (v.row + 1, v.col) == (vertex.row, vertex.col)
                ),
                None,
            )
        )
    # left
    if v.col > 0 and GRID[v.row][v.col - 1] - GRID[v.row][v.col] == 1:
        result.append(
            next(
                (
                    vertex
                    for vertex in vertices
                    if (v.row, v.col - 1) == (vertex.row, vertex.col)
                ),
                None,
            )
        )
    # right
    if v.col < GRID_WIDTH - 1 and GRID[v.row][v.col + 1] - GRID[v.row][v.col] == 1:
        result.append(
            next(
                (
                    vertex
                    for vertex in vertices
                    if (v.row, v.col + 1) == (vertex.row, vertex.col)
                ),
                None,
            )
        )
    return result


def bfs(s: Vertex) -> int:
    queue = [s]
    vertices = [
        Vertex(row, col) for row in range(GRID_HEIGHT) for col in range(GRID_WIDTH)
    ]

    while len(queue):
        u = queue.pop(0)

        for v in neighbours(u, vertices):
            if v.colour == VertexColour.WHITE:
                v.colour = VertexColour.GREY
                v.paths = u.paths
                v.predecessor = u

                queue.append(v)
            else:
                v.paths += u.paths
        u.colour = VertexColour.BLACK

    return sum(
        [
            vertex.paths
            for vertex in vertices
            if vertex.colour == VertexColour.BLACK and vertex in TRAILTAILS
        ]
    )


submit(sum([bfs(trailhead) for trailhead in TRAILHEADS]))
