from dataclasses import dataclass
import itertools
import math
from typing import List, Union


data = "2333133121414131402"

FREE_BLOCK = -1


@dataclass
class DiskBlock:
    id: int
    size: int

    def free(self):
        self.id = FREE_BLOCK


class Disk:
    blocks: List[DiskBlock]

    def __init__(self, disk_map: str):
        self.blocks = self._to_disk_blocks(disk_map)

    def _to_block_map(self) -> List[int]:
        block_map: List[int] = []

        for block in self.blocks:
            if block.id == FREE_BLOCK:
                block_map.extend([FREE_BLOCK] * block.size)
            else:
                block_map.extend([block.id] * block.size)
        return block_map

    def _disk_map_to_block_map_string(self, disk_map: str) -> str:
        block_map: List[int] = []

        for index, char in enumerate(disk_map):
            if index % 2:
                block_map.extend([FREE_BLOCK] * int(char))
            else:
                block_map.extend([(index // 2)] * int(char))
        return block_map

    def _to_disk_blocks(self, input_map: str, convert=True) -> List[DiskBlock]:
        block_map = (
            self._disk_map_to_block_map_string(input_map) if convert else input_map
        )

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

        if target_block.size < source_block.size:
            raise Exception("Target block doesn't have enough free space")

        # swap blocks of the same size
        if target_block.size == source_block.size:
            self.blocks[target_block_index], self.blocks[source_block_index] = (
                self.blocks[source_block_index],
                self.blocks[target_block_index],
            )
        else:
            self.blocks.pop(target_block_index)

            self.blocks.insert(
                target_block_index,
                DiskBlock(id=FREE_BLOCK, size=target_block.size - source_block.size),
            )

            self.blocks.insert(
                target_block_index,
                DiskBlock(id=source_block.id, size=source_block.size),
            )

            source_block.free()

        # update blocks
        self.blocks = self._to_disk_blocks(self._to_block_map(), convert=False)

    def _find_free_block(self, min_size: int) -> Union[int, None]:
        for index, block in enumerate(self.blocks):
            if block.size >= min_size and block.id == FREE_BLOCK:
                return index
        return None

    def _find_rightmost_occupied_block(self, max_id: int) -> Union[int, None]:
        for index, block in reversed(list(enumerate(self.blocks))):
            if block.id <= max_id and block.id != FREE_BLOCK:
                return index
        return None

    def defragment(self) -> None:
        source_block_index = self._find_rightmost_occupied_block(math.inf)

        while source_block_index is not None and source_block_index > 0:
            target_block_index = self._find_free_block(
                self.blocks[source_block_index].size
            )

            if target_block_index is None or target_block_index >= source_block_index:
                source_block_index = self._find_rightmost_occupied_block(
                    self.blocks[source_block_index].id - 1
                )
                continue
            print()
            print(
                "[MOVE]",
                self.blocks[source_block_index],
                "-> ",
                self.blocks[target_block_index],
            )
            print()

            self._move_block(source_block_index, target_block_index)
            print(self)

            source_block_index = self._find_rightmost_occupied_block(
                self.blocks[source_block_index].id - 1
            )

            # print("NEW SOURCE: ", self.blocks[source_block_index])

        print("Done")

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
disk.defragment()
# print(disk)
