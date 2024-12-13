from typing import List
from functools import cache

from aocd import data, submit


N = 75


@cache
def blink(stone: str) -> tuple[str, ...]:
    result = []

    if stone == "0":
        result.append("1")
    elif len(stone) % 2 == 0:
        result.append(str(int(stone[: len(stone) // 2])))
        result.append(str(int(stone[len(stone) // 2 :])))
    else:
        result.append(str(int(stone) * 2024))
    return tuple(result)


def itemize(stones: List[str]) -> dict[str, int]:
    itemized_stones = dict()

    for stone in stones:
        if stone in itemized_stones:
            itemized_stones[stone] += 1
        else:
            itemized_stones[stone] = 1
    return itemized_stones


def apply_blink_to_stones(stones: dict[str, int]) -> dict[str, int]:
    result = {}

    for key, value in stones.items():
        blinked_stones = blink(key)

        for blinked_stone in blinked_stones:
            if blinked_stone in result:
                result[blinked_stone] += value
            else:
                result[blinked_stone] = value
    return result


def iterative_blink(stones: dict[str, int], number: int) -> dict[str, int]:
    result = stones.copy()
    for _ in range(number):
        result = apply_blink_to_stones(result)
    return result


def number_of_stones(stones: dict[str, int]) -> int:
    return sum(stones.values())


itemized_stones = itemize(data.split())
itemized_stones = iterative_blink(itemized_stones, N)

submit(number_of_stones(itemized_stones))
