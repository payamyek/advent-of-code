from dataclasses import dataclass
from typing import List, Self, Union
from aocd import data
import itertools

data = "2333133121414131402"

FREE_SPACE = -1


@dataclass
class DiskBlock:
    span: int
    value: int

    def consume_free_space(self, other: Self) -> List[Self]:
        if self.value != FREE_SPACE:
            raise Exception("Disk block is not free")

        if self.span < other.span:
            raise Exception("Disk block doesn't have enough free space")

        splitted_blocks = []

        self.value = other.value

        if self.span == other.span:
            other.free()
            splitted_blocks.append(self)
        else:
            free_block = DiskBlock(self.span - other.span, FREE_SPACE)
            self.span = other.span
            other.free()
            splitted_blocks.extend([self, free_block])

        return splitted_blocks

    def free(self):
        self.value = FREE_SPACE


class Disk:
    blocks: List[DiskBlock]

    def __init__(self, disk_map: str):
        self.blocks = self._to_disk_blocks(disk_map)

    def _disk_map_to_block_map(self, disk_map: str) -> List[int]:
        block_map: List[int] = []

        for index, char in enumerate(disk_map):
            if index % 2:
                block_map.extend([FREE_SPACE] * int(char))
            else:
                block_map.extend([(index // 2)] * int(char))

        return block_map

    def _to_disk_blocks(self, disk_map: str) -> List[DiskBlock]:
        disk_slots = []
        block_map = self._disk_map_to_block_map(disk_map)

        for key, group in itertools.groupby(block_map):
            span = len(list(group))
            disk_slots.append(DiskBlock(span, key))
        return disk_slots

    def leftmost_free_disk_block(self, span: int) -> Union[DiskBlock, None]:
        for disk_slot in self.blocks:
            if disk_slot.value == FREE_SPACE and disk_slot.span >= span:
                return disk_slot
        return None

    def find_block_index(self, disk_block: DiskBlock) -> int:
        index = -1
        try:
            index = disk.blocks.index(disk_block)
        except ValueError:
            pass
        return index

    def checksum(self) -> int:
        total = 0
        index_from_right = 0

        for index, block in reversed(list(enumerate(self.blocks))):
            free_block = self.leftmost_free_disk_block(block.span)
            splitted_blocks = free_block.consume_free_space(block)

            free_block_index = self.find_block_index(free_block)
            self.blocks.remove(free_block)

            if free_block_index == -1:
                break

            for splitted_block in reversed(splitted_blocks):
                self.blocks.insert(free_block_index, splitted_block)

            break

            index_from_right += 1

        return total

    def __str__(self) -> str:
        result = ""
        for block in self.blocks:
            result += block.span * ("." if block.value == -1 else str(block.value))
        return result


disk = Disk(data)

# print(*disk.blocks, sep="\n")

disk.checksum()

print(disk)
