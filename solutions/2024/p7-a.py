import itertools
from typing import List
from aocd import data, submit


total_to_nums_map = {
    int(row.split(":")[0]): list(map(int, row.split(":")[1].split()))
    for row in data.splitlines()
}


def verifier(nums: List[int], target: int) -> bool:
    for operations in list(itertools.product(["+", "*"], repeat=len(nums) - 1)):
        result = nums[0]
        for num, operation in zip(nums[1:], operations):
            if operation == "+":
                result += num
            else:
                result *= num

        if result == target:
            return True
    return False


submit(sum([key for key in total_to_nums_map if verifier(total_to_nums_map[key], key)]))
