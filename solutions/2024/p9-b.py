from dataclasses import dataclass
from typing import List, Self, Union
from aocd import data
import itertools

data = "2333133121414131402"

FREE_SPACE = -1


@dataclass
class DiskBlock:
    span: int
    id: int

    def consume_free_space(self, other: Self) -> List[Self]:
        if self.id != FREE_SPACE:
            raise Exception("Disk block is not free")

        if self.span < other.span:
            raise Exception("Disk block doesn't have enough free space")

        splitted_blocks = []

        self.id = other.id

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
        self.id = FREE_SPACE


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
            if disk_slot.id == FREE_SPACE and disk_slot.span >= span:
                return disk_slot
        return None

    def rightmost_disk_block(self, max_id: int) -> Union[DiskBlock, None]:
        for disk_slot in reversed(self.blocks):
            if disk_slot.id != FREE_SPACE and disk_slot.id <= max_id:
                return disk_slot
        return None

    def find_block_index(self, disk_block: DiskBlock) -> int:
        index = -1
        try:
            index = disk.blocks.index(disk_block)
        except ValueError:
            pass
        return index

    def fragment(self) -> None:
        source_disk_block = self.rightmost_disk_block(len(self.blocks))
        target_disk_block = self.leftmost_free_disk_block(source_disk_block.span)

        splitted_blocks = target_disk_block.consume_free_space(source_disk_block)

        target_disk_block_index = self.find_block_index(target_disk_block)

        self.blocks.remove(target_disk_block)

        for splitted_block in reversed(splitted_blocks):
            self.blocks.insert(target_disk_block_index, splitted_block)

        source_disk_block.free()

    def __str__(self) -> str:
        result = ""
        for block in self.blocks:
            result += block.span * ("." if block.id == -1 else str(block.id))
        return result


disk = Disk(data)
print(disk)


disk.fragment()

print(disk)
