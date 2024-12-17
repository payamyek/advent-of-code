from dataclasses import dataclass
from typing import List
from aocd import data, submit
from collections import Counter

GRID = [list(row) for row in data.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])


@dataclass(frozen=True)
class Vertex:
    row: int
    col: int
    plant: str

    # UPDATE GLOBAL VARIABLE TO TRACK GRIDVERTEX -> VERTEX MAPPING
    def __post_init__(self):
        for gv in to_grid_vertices(self):
            if grid_vertices_to_vertices.get(gv) is None:
                grid_vertices_to_vertices[gv] = set([self])
            else:
                grid_vertices_to_vertices[gv].add(self)


@dataclass(frozen=True)
class GridVertex:
    row: int
    col: int


# MAPS EACH GRID VERTEX TO ALL VERTICES IT TOUCHES
grid_vertices_to_vertices: dict[GridVertex, set[Vertex]] = dict()


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


def find_regions() -> List[set[Vertex]]:
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


def to_grid_vertices(v: Vertex) -> set[GridVertex]:
    return (
        GridVertex(v.row, v.col),
        GridVertex(v.row, v.col + 1),
        GridVertex(v.row + 1, v.col),
        GridVertex(v.row + 1, v.col + 1),
    )


def fence_cost(region: set[Vertex]) -> int:
    grid_vertices: list[GridVertex] = []

    for vertex in region:
        grid_vertices.extend(to_grid_vertices(vertex))

    sides = 0

    for grid_vertex, count in Counter(grid_vertices).items():
        # ALL GRID VERTICES WITH 1 OR 3 INTERSECTIONS ARE SIDES
        if count in [1, 3]:
            sides += 1
        # GRID VERTICES WITH 2 INTERSECTIONS MIGHT BE SIDES
        elif count == 2:
            plant = next(iter(region)).plant

            # VERTICES WITH SAME PLANT TYPE
            v1, v2 = list(
                filter(
                    lambda x: x.plant == plant, grid_vertices_to_vertices[grid_vertex]
                )
            )

            # VERTICES ARE DIAGONAL NEIGHBOURS
            if abs(v1.row - v2.row) == 1 and abs(v1.col - v2.col) == 1:
                sides += 2

    return len(region) * sides


regions = find_regions()
total_cost = sum([fence_cost(region) for region in regions])
submit(total_cost)
