from typing import List
from aocd import data, submit
import re

ordering_rules = {}

for match in re.findall(r"(\d+)\|(\d+)", data.split("\n\n")[0]):
    x, y = int(match[0]), int(match[1])
    if ordering_rules.get(x) is None:
        ordering_rules[x] = {y}
    else:
        ordering_rules[x].add(y)


pages_to_produce = []

for match in re.findall(r"[\d+,]+[\d+]|\d+", data.split("\n\n")[1]):
    pages_to_produce.append(list(map(int, match.split(","))))


def is_valid_production(input: List[int]) -> bool:
    numbers_before = set()
    for num in input:
        numbers_before.add(num)
        if bool(numbers_before & ordering_rules.get(num, set())):
            return False
    return True


invalid_productions = []

for production in pages_to_produce:
    if not is_valid_production(production):
        invalid_productions.append(production)


def safe_index(value, input):
    try:
        index_value = input.index(value)
    except ValueError:
        index_value = -1
    return index_value


def fix_production(input: List[int]) -> List[int]:
    fixed_input = input.copy()

    for index in range(len(fixed_input) - 1):
        for cursor in range(index + 1, len(fixed_input)):
            if fixed_input[index] in ordering_rules.get(fixed_input[cursor], set()):
                fixed_input[index], fixed_input[cursor] = (
                    fixed_input[cursor],
                    fixed_input[index],
                )
    return fixed_input


fixed_productions = [
    fix_production(invalid_production) for invalid_production in invalid_productions
]


total = sum([production[len(production) // 2] for production in fixed_productions])

submit(total)
