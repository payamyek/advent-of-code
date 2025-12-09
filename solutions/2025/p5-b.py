from collections import namedtuple
from typing import List
from aocd import data, submit

Interval = namedtuple("Interval", "start end")


def generate_intervals() -> List[Interval]:
    fresh, _ = data.split("\n\n")
    return [
        Interval(int(it.split("-")[0]), int(it.split("-")[1])) for it in fresh.split()
    ]


def merge_intervals(range1: Interval, range2: Interval) -> List[Interval]:
    # range 2 is contained within range 1
    if range2.start >= range1.start and range2.end <= range1.end:
        return [range1]
    # range1 is contained within range 2
    elif range1.start >= range2.start and range1.end <= range2.end:
        return [range2]
    # range 2 intersects range 1 from the left side
    elif range2.end <= range1.end and range2.end >= range1.start:
        return [Interval(range2.start, range1.end)]
    # range 2 intersects range 1 from the right side
    elif range2.start <= range1.end and range2.start >= range1.start:
        return [Interval(range1.start, range2.end)]
    return [range1, range2]


def solve():
    intervals = sorted(generate_intervals(), key=lambda it: it.start)
    index = 0

    while index + 1 < len(intervals):
        merged_intervals = merge_intervals(intervals[index], intervals[index + 1])
        is_disjoint = len(merged_intervals) == 2

        if is_disjoint:
            index += 1
            continue

        intervals.pop(index + 1)
        intervals[index] = merged_intervals[0]

    return sum(1 + interval.end - interval.start for interval in intervals)


submit(solve())
