from collections import namedtuple
from aocd import data, submit


Pantry = namedtuple("Panty", "fresh available")


def generate_pantry() -> Pantry:
    fresh, available = data.split("\n\n")

    fresh = [(int(it.split("-")[0]), int(it.split("-")[1])) for it in fresh.split()]
    available = [int(it) for it in available.split()]

    return Pantry(fresh, available)


def is_fresh(pantry: Pantry, ingredient: int) -> bool:
    for start, end in pantry.fresh:
        if start <= ingredient <= end:
            return True
    return False


def solve():
    pantry = generate_pantry()
    fresh_available = [it for it in pantry.available if is_fresh(pantry, it)]
    return len(fresh_available)


submit(solve())
