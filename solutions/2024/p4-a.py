from aocd import data, submit


WORD = "XMAS"

CROSSWORD = [list(row) for row in data.splitlines()]


def horizontal_matches() -> int:
    matches = 0
    for i in range(len(CROSSWORD)):
        for j in range(len(CROSSWORD[i]) - len(WORD) + 1):
            entry = "".join(CROSSWORD[i][j : j + 4])
            if entry == WORD or entry == WORD[::-1]:
                matches += 1
            # print(entry)
    return matches


def vertical_matches() -> int:
    matches = 0
    for i in range(len(CROSSWORD) - len(WORD) + 1):
        for j in range(len(CROSSWORD[i])):
            entry = ""
            for offset in range(len(WORD)):
                entry += CROSSWORD[i + offset][j]

            if entry == WORD or entry == WORD[::-1]:
                matches += 1
            # print(entry)
    return matches


def right_diagonal_matches() -> int:
    matches = 0
    for i in range(len(CROSSWORD) - len(WORD) + 1):
        for j in range(len(WORD) - 1, len(CROSSWORD[i])):
            entry = ""
            for offset in range(len(WORD)):
                entry += CROSSWORD[i + offset][j - offset]

            if entry == WORD or entry == WORD[::-1]:
                matches += 1
            print(entry)
    return matches


def left_diagonal_matches() -> int:
    matches = 0
    for i in range(len(CROSSWORD) - len(WORD) + 1):
        for j in range(len(CROSSWORD[i]) - len(WORD) + 1):
            entry = ""
            for offset in range(len(WORD)):
                entry += CROSSWORD[i + offset][j + offset]

            if entry == WORD or entry == WORD[::-1]:
                matches += 1
    return matches


total = (
    horizontal_matches()
    + vertical_matches()
    + right_diagonal_matches()
    + left_diagonal_matches()
)

submit(total)
