from dataclasses import dataclass
import itertools
from typing import List, Union


data = "2333133121414131402"

FREE_BLOCK = -1


@dataclass
class DiskBlock:
    id: int
    size: int

    def free(self):
        self.size = FREE_BLOCK


class Disk:
    blocks: List[DiskBlock]

    def __init__(self, disk_map: str):
        self.blocks = self._to_disk_blocks(disk_map)

    def defragment(self) -> None:
        pass

    def _to_block_map(self) -> List[int]:
        block_map: List[int] = []

        for block in self.blocks:
            if block.id == FREE_BLOCK:
                block_map.extend([FREE_BLOCK] * block.size)
            else:
                block_map.extend([block.id] * block.size)
        return block_map

    def _disk_map_to_block_map(self, disk_map: str) -> str:
        block_map: List[int] = []

        for index, char in enumerate(disk_map):
            if index % 2:
                block_map.extend([FREE_BLOCK] * int(char))
            else:
                block_map.extend([(index // 2)] * int(char))
        return block_map

    def _to_disk_blocks(self, input_map: str, convert=True) -> List[DiskBlock]:
        block_map = self._disk_map_to_block_map(input_map) if convert else input_map

        return [
            DiskBlock(id=key, size=len(list(group)))
            for key, group in itertools.groupby(block_map)
        ]

    def _move_block(self, source_block_index: int, target_block_index: int) -> None:
        source_block, target_block = (
            self.blocks[source_block_index],
            self.blocks[target_block_index],
        )

        if target_block.id != FREE_BLOCK:
            raise Exception("Target block is not free")

        if target_block.size > source_block.size:
            raise Exception("Target block doesn't have enough free space")

        # swap blocks of the same size
        if target_block.size == source_block.size:
            self.blocks[target_block_index], self.blocks[source_block_index] = (
                self.blocks[source_block_index],
                self.blocks[target_block_index],
            )

            # update blocks
            self.blocks = self._to_disk_blocks(self._to_block_map(), convert=False)

    def find_compatible_free_block(self, min_size: int) -> Union[int, None]:
        for index, block in enumerate(self.blocks):
            if block.size >= min_size:
                return index
        return None

    def checksum(self) -> int:
        return sum(
            [
                block.id * index
                for index, block in enumerate(self.blocks)
                if block.id != FREE_BLOCK
            ]
        )

    def __str__(self):
        return "".join(
            map(lambda x: "." if x == FREE_BLOCK else str(x), self._to_block_map())
        )


disk = Disk(data)

print(disk)

free_block = disk.find_compatible_free_block(3)

disk._move_block(2, 1)

print(disk)
print(*disk.blocks, sep="\n")
