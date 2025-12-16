from collections import namedtuple
from typing import List
from aocd import data, submit

LEFT = "L"
RIGHT = "R"
STARTING_DIAL_POS = 50
DIALS = 100


Rotation = namedtuple("Rotation", "direction units")

data: List[Rotation] = [Rotation(item[0], int(item[1:])) for item in data.split()]


def move(rotation: Rotation, dial_pos: int):
    return (rotation.units * (-1 if rotation.direction == LEFT else 1) + dial_pos) % 100


def solve() -> int:
    total = 0
    cur_pos = STARTING_DIAL_POS

    for rotation in data:
        next_pos = move(rotation, cur_pos)

        total += rotation.units // DIALS
        transformed_rotation = Rotation(rotation.direction, rotation.units % DIALS)

        if transformed_rotation.units <= DIALS and cur_pos != 0:
            if next_pos == 0:
                total += 1
            elif transformed_rotation.direction == LEFT and next_pos >= cur_pos:
                total += 1
            elif transformed_rotation.direction == RIGHT and next_pos <= cur_pos:
                total += 1

        cur_pos = next_pos

    return total


submit(solve())
