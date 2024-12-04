from aocd import data, submit


WORD = "MAS"

CROSSWORD = [list(row) for row in data.splitlines()]


def left_diagonal_match(x: int, y: int):
    entry = CROSSWORD[x][y] + CROSSWORD[x + 1][y - 1] + CROSSWORD[x + 2][y - 2]
    return entry == WORD or entry == WORD[::-1]


def right_diagonal_match(x: int, y: int):
    entry = CROSSWORD[x][y] + CROSSWORD[x + 1][y + 1] + CROSSWORD[x + 2][y + 2]
    return entry == WORD or entry == WORD[::-1]


total = 0

for i in range(len(CROSSWORD) - len(WORD) + 1):
    for j in range(len(CROSSWORD[i]) - len(WORD) + 1):
        if right_diagonal_match(i, j) and left_diagonal_match(i, j + 2):
            total += 1

submit(total)
