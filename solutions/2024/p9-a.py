from aocd import data

FREE_SPACE = "."

data = "2333133121414131402"


def disk_map_to_block_map(disk_map: str) -> str:
    return "".join(
        [
            int(char) * FREE_SPACE if index % 2 else int(char) * str(index // 2)
            for index, char in enumerate(disk_map)
        ]
    )


def shift_blocks(block_map: str) -> str:
    result = list(block_map)

    for index, char in reversed(list(enumerate(block_map))):
        if not char.isdigit():
            continue

        # leftmost free spot
        free_block_index = result.index(FREE_SPACE) if FREE_SPACE in result else -1

        # finished sorted
        if free_block_index >= index:
            break

        if free_block_index >= 0:
            result[index] = FREE_SPACE
            result[free_block_index] = char
    return "".join(result)


def compute_checksum(block_map: str) -> int:
    return sum(
        [index * int(char) for index, char in enumerate(block_map) if char.isdigit()]
    )


block_map = disk_map_to_block_map(data)
shifted_block_map = shift_blocks(block_map)
checksum = compute_checksum(shifted_block_map)

print(checksum)