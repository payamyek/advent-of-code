from aocd import data
import re

print(data)


GRID = [list(row) for row in data.splitlines()]

WIDTH = len(list(data.splitlines()[0]))

data = "".join(data.splitlines())


matches_to_verify = []

for match in re.finditer(r"(\d+)", data):
    start_index, end_index = match.span()

    matches_to_verify.append(
        {
            "value": int(match.group()),
            "row": start_index // WIDTH,
            "column": start_index % WIDTH,
            "span": end_index - start_index,
        }
    )


def is_symbol(input: str) -> bool:
    return not input.isdigit() and input != "."


def is_adjacent_to_symbol(row: int, col: int) -> bool:
    # left
    if col > 0 and is_symbol(GRID[row][col - 1]):
        return True
    # right
    elif col < WIDTH - 1 and is_symbol(GRID[row][col + 1]):
        return True
    # up
    elif row > 0 and is_symbol(GRID[row - 1][col]):
        return True
    # down
    elif row < len(GRID) - 1 and is_symbol(GRID[row + 1][col]):
        return True
    # up left
    elif row > 0 and col > 0 and is_symbol(GRID[row - 1][col - 1]):
        return True
    # up right
    elif row > 0 and col < WIDTH - 1 and is_symbol(GRID[row - 1][col + 1]):
        return True
    # down left
    elif row < len(GRID) - 1 and col > 0 and is_symbol(GRID[row + 1][col - 1]):
        return True
    # down right
    elif row < WIDTH - 1 and col < len(GRID) - 1 and is_symbol(GRID[row + 1][col + 1]):
        return True
    return False


total = 0

# print("width", WIDTH)
# print(GRID[96])

for match in matches_to_verify:
    print(match)
    for offset in range(match["span"]):
        if is_adjacent_to_symbol(match["row"], match["column"] + offset):
            total += match["value"]
            break


# print(total)
