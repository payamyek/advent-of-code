from aocd import data, submit


data = [list(row) for row in data.split()]


PAPER = "@"
REMOVED = "X"
HEIGHT = len(data)
WIDTH = len(data[0])


def adjacent_neighbours(row: int, col: int):
    if data[row][col] != PAPER:
        raise ValueError("Cannot be called for non-paper cells")

    neighbours = []

    if row > 0 and data[row - 1][col] == PAPER:  # up
        neighbours.append((row - 1, col))
    if row > 0 and col > 0 and data[row - 1][col - 1] == PAPER:  # up left
        neighbours.append((row - 1, col - 1))
    if row > 0 and col < WIDTH - 1 and data[row - 1][col + 1] == PAPER:  # up right
        neighbours.append((row - 1, col + 1))
    if col > 0 and data[row][col - 1] == PAPER:  # left
        neighbours.append((row, col - 1))
    if col < WIDTH - 1 and data[row][col + 1] == PAPER:  # right
        neighbours.append((row, col + 1))
    if row < HEIGHT - 1 and data[row + 1][col] == PAPER:  # down
        neighbours.append((row + 1, col))
    if row < HEIGHT - 1 and col > 0 and data[row + 1][col - 1] == PAPER:  # down left
        neighbours.append((row + 1, col - 1))
    if (
        row < HEIGHT - 1 and col < WIDTH - 1 and data[row + 1][col + 1] == PAPER
    ):  # down right
        neighbours.append((row + 1, col + 1))

    return neighbours


def removable_paper():
    return [
        (row, col)
        for row in range(HEIGHT)
        for col in range(WIDTH)
        if data[row][col] == PAPER and len(adjacent_neighbours(row, col)) < 4
    ]


def solve():
    total = 0

    while len(removable := removable_paper()) > 0:
        for row, col in removable:
            data[row][col] = REMOVED
            total += 1
    return total


submit(solve())
