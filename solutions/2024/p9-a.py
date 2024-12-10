from typing import List
from aocd import data, submit


FREE_SPACE = -1


def disk_map_to_block_map(disk_map: str) -> List[int]:
    block_map: List[int] = []

    for index, char in enumerate(disk_map):
        if index % 2:
            block_map.extend([FREE_SPACE] * int(char))
        else:
            block_map.extend([(index // 2)] * int(char))

    return block_map


def compute_checksum(block_map: List[int]) -> int:
    total = 0

    for index, block_id in enumerate(block_map):
        if block_id != -1:
            total += index * block_id
            continue

        filled_indices = [
            index for index, block_id in enumerate(block_map) if block_id != -1
        ]

        if (
            not len(filled_indices)
            or (rightmost_block_index := filled_indices[-1]) <= index
        ):
            break

        total += block_map[rightmost_block_index] * index
        block_map[rightmost_block_index] = FREE_SPACE

    return total


block_map = disk_map_to_block_map(data)
checksum = compute_checksum(block_map)
submit(checksum)
