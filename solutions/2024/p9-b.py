from dataclasses import dataclass
from typing import List
from aocd import data
import itertools

data = "12345"

FREE_SPACE = -1


@dataclass(frozen=True)
class DiskSlot:
    index: int
    span: int
    value: int


def disk_map_to_block_map(disk_map: str) -> List[int]:
    block_map: List[int] = []

    for index, char in enumerate(disk_map):
        if index % 2:
            block_map.extend([FREE_SPACE] * int(char))
        else:
            block_map.extend([(index // 2)] * int(char))

    return block_map


def find_rightmost_block_index(block_map: List[int], last_block_index=-1) -> int:
    start_index = last_block_index - 1 if last_block_index != -1 else len(block_map) - 1

    for index in range(start_index, -1, -1):
        if block_map[index] != -1:
            return index
    return -1


def compute_checksum(block_map: List[int]) -> int:
    block_map = block_map.copy()
    rightmost_block_index = -1

    total = 0

    for index, block_id in enumerate(block_map):
        if block_id != -1:
            total += index * block_id
            continue

        rightmost_block_index = find_rightmost_block_index(
            block_map, rightmost_block_index
        )

        if rightmost_block_index == -1 or rightmost_block_index <= index:
            break

        total += block_map[rightmost_block_index] * index
        block_map[rightmost_block_index] = FREE_SPACE

    return total


def find_disk_slots(block_map: List[int]) -> List[DiskSlot]:
    disk_slots = []
    index = 0

    for key, group in itertools.groupby(block_map):
        span = len(list(group))
        disk_slots.append(DiskSlot(index, span, key))
        index += span
    return disk_slots


block_map = disk_map_to_block_map(data)
checksum = compute_checksum(block_map)
disk_slots = find_disk_slots(block_map)

print(block_map)
print(disk_slots)