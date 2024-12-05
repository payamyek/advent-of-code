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


valid_productions = []

for production in pages_to_produce:
    if is_valid_production(production):
        valid_productions.append(production)

total = sum([production[len(production) // 2] for production in valid_productions])

submit(total)
