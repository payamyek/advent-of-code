from typing import List
from aocd import data, submit


def is_increasing_or_decreasing(input: List[int]) -> bool:
    return sorted(input) == input or sorted(input, reverse=True) == input


def satisfies_adjacent_rules(input: List[int]) -> bool:
    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
            return False
        elif abs(input[i] - input[i + 1]) > 3:
            return False
    return True


total = 0


for row in data.splitlines():
    row_items = [int(item) for item in row.split()]

    if is_increasing_or_decreasing(row_items) and satisfies_adjacent_rules(row_items):
        total += 1
        continue

    for i in range(len(row_items)):
        row_items_with_missing_item = [
            item for index, item in enumerate(row_items) if index != i
        ]

        if is_increasing_or_decreasing(
            row_items_with_missing_item
        ) and satisfies_adjacent_rules(row_items_with_missing_item):
            total += 1
            break


submit(total)
