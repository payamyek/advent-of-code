from typing import List

from aocd import data, submit


def blink(stones: List[int]) -> List[int]:
    new_stones = []

    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            new_stones.append(str(int(stone[: len(stone) // 2])))
            new_stones.append(str(int(stone[len(stone) // 2 :])))
        else:
            new_stones.append(str(int(stone) * 2024))

    return new_stones


def blink_number_of_times(stones: List[int], number: int) -> List[int]:
    result = stones[:]
    for _ in range(number):
        result = blink(result)
    return result


result = blink_number_of_times(data.split(), 25)
submit(len(result))
