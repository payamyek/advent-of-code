from collections import namedtuple, deque
from aocd import data, submit

START_CELL = "S"
EMPTY_CELL = "."
SPLITTER_CELL = "^"
TACHYON_BEAM = "|"


GRID = [list(row) for row in data.split()]
HEIGHT = len(GRID)
WIDTH = len(GRID[0])

Cell = namedtuple("Cell", "row col")


def find_start_cell() -> Cell:
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if GRID[i][j] == START_CELL:
                return Cell(i, j)
    return Cell(0, 0)


def total_beam_splits():
    total = 0

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if GRID[i][j] == SPLITTER_CELL and GRID[i - 1][j] == TACHYON_BEAM:
                total += 1
    return total


def solve():
    dq = deque([find_start_cell()])

    while len(dq):
        cell = dq.popleft()

        if cell.row + 1 >= HEIGHT:
            continue

        if GRID[cell.row + 1][cell.col] == SPLITTER_CELL:
            neighbours = [
                Cell(cell.row + 1, cell.col - 1),
                Cell(cell.row + 1, cell.col + 1),
            ]

            for v in neighbours:
                if GRID[v.row][v.col] == EMPTY_CELL:
                    GRID[v.row][v.col] = TACHYON_BEAM
                    dq.append(v)

        else:
            GRID[cell.row + 1][cell.col] = TACHYON_BEAM
            dq.append(Cell(cell.row + 1, cell.col))

    return total_beam_splits()


submit(solve())
