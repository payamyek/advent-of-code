from dataclasses import dataclass
from typing import List, Union
from aocd import data
import itertools

data = "2333133121414131402"

FREE_SPACE = -1


@dataclass
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


def find_disk_slots(block_map: List[int]) -> List[DiskSlot]:
    disk_slots = []
    index = 0

    for key, group in itertools.groupby(block_map):
        span = len(list(group))
        disk_slots.append(DiskSlot(index, span, key))
        index += span
    return disk_slots


def find_leftmost_free_disk_slot(
    disk_slots: List[DiskSlot], disk_slot_to_move: DiskSlot
) -> Union[DiskSlot, None]:
    for disk_slot in disk_slots:
        if disk_slot.value == -1 and disk_slot.span == disk_slot_to_move.span:
            return disk_slot
    return None


def compute_checksum(block_map: List[int]) -> int:
    disk_slots = find_disk_slots(block_map)

    for disk_slot in reversed(find_disk_slots(block_map)):
        if disk_slot.value == -1:
            continue

        free_disk_slot = find_leftmost_free_disk_slot(disk_slots, disk_slot)

        if free_disk_slot is None:
            continue

        print(f"{disk_slot} can be moved to {free_disk_slot} ")


block_map = disk_map_to_block_map(data)
compute_checksum(block_map)
