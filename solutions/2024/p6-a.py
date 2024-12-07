from aocd import data, submit


# ---------- CONSTANTS - START ----------
DIRECTION_UP = "^"
DIRECTION_DOWN = "v"
DIRECTION_LEFT = "<"
DIRECTION_RIGHT = ">"

DIRECTIONS = [DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT]

UNVISITED_SPOT = "."
VISITED_SPOT = "X"
OBSTACLE = "#"

MOVE_OUTCOME_GUARD_FREE = "MOGF"
MOVE_OUTCOME_OBSTACLE = "MOO"
MOVE_OUTCOME_DEFAULT = "MOD"

GRID = [list(row) for row in data.splitlines()]

GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])
# ---------- CONSTANTS - END ----------


def find_guard() -> tuple[tuple[int, int], str]:
    for row in range(len(GRID)):
        for col in range(len(GRID[row])):
            if GRID[row][col] in DIRECTIONS:
                return (row, col), GRID[row][col]


def check_guard_at_position(row: int, col: int):
    if GRID[row][col] not in DIRECTIONS:
        raise Exception("Grid Position Doesn't Contain Guard")


def _is_guard_free(row: int, col: int) -> bool:
    check_guard_at_position(row, col)

    direction = GRID[row][col]

    if row == 0 and direction == DIRECTION_UP:
        return True
    elif row == GRID_HEIGHT - 1 and direction == DIRECTION_DOWN:
        return True
    elif col == GRID_WIDTH - 1 and DIRECTION_RIGHT:
        return True
    elif col == 0 and direction == DIRECTION_LEFT:
        return True
    return False


def _is_facing_obstacle(row: int, col: int) -> bool:
    check_guard_at_position(row, col)

    direction = GRID[row][col]

    if direction == DIRECTION_UP and row > 0 and GRID[row - 1][col] == OBSTACLE:
        return True
    elif (
        direction == DIRECTION_DOWN
        and row < GRID_HEIGHT - 1
        and GRID[row + 1][col] == OBSTACLE
    ):
        return True
    elif (
        direction == DIRECTION_RIGHT
        and col < GRID_WIDTH - 1
        and GRID[row][col + 1] == OBSTACLE
    ):
        return True
    elif direction == DIRECTION_LEFT and col > 0 and GRID[row][col - 1] == OBSTACLE:
        return True
    return False


def turn_right_ninety_degrees(row: int, col: int):
    check_guard_at_position(row, col)
    current_direction_index = DIRECTIONS.index(GRID[row][col])
    GRID[row][col] = DIRECTIONS[(current_direction_index + 1) % len(DIRECTIONS)]


def move_outcome(row: int, col: int) -> str:
    if _is_guard_free(row, col):
        return MOVE_OUTCOME_GUARD_FREE
    elif _is_facing_obstacle(row, col):
        return MOVE_OUTCOME_OBSTACLE
    return MOVE_OUTCOME_DEFAULT


def perform_default_move(row: int, col: int) -> tuple[int, int]:
    check_guard_at_position(row, col)
    direction = GRID[row][col]
    new_guard_position = None

    # mark current spot as visited
    GRID[row][col] = VISITED_SPOT

    if direction == DIRECTION_UP:
        GRID[row - 1][col] = direction
        new_guard_position = (row - 1, col)
    elif direction == DIRECTION_DOWN:
        GRID[row + 1][col] = direction
        new_guard_position = (row + 1, col)
    elif direction == DIRECTION_LEFT:
        GRID[row][col - 1] = direction
        new_guard_position = (row, col - 1)
    else:
        GRID[row][col + 1] = direction
        new_guard_position = (row, col + 1)
    return new_guard_position


(guard_row, guard_col), guard_direction = find_guard()

while (move := move_outcome(guard_row, guard_col)) != MOVE_OUTCOME_GUARD_FREE:
    if move == MOVE_OUTCOME_DEFAULT:
        guard_row, guard_col = perform_default_move(guard_row, guard_col)
    elif move == MOVE_OUTCOME_OBSTACLE:
        turn_right_ninety_degrees(guard_row, guard_col)


submit(sum([row.count(VISITED_SPOT) for row in GRID]) + 1)
