data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

data = [list(row) for row in data.split()]


PAPER = "@"
HEIGHT = len(data)
WIDTH = len(data[0])


def adjacent_neighbours(input: str, row: int, col: int):
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


def solve(input):
    return sum(
        [
            1
            for row in range(HEIGHT)
            for col in range(WIDTH)
            if input[row][col] == PAPER
            and len(adjacent_neighbours(input, row, col)) < 4
        ]
    )
