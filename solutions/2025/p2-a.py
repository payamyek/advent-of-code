from aocd import data, submit

data = [it for it in data.split(",")]


def is_invalid(str_num: str):
    if len(str_num) % 2 != 0:
        return False

    mid = len(str_num) // 2

    left_str, right_str = str_num[0:mid], str_num[mid:]

    if left_str[0] == "0":
        return False

    return left_str == right_str


def enumerate_all_ids(range_str: str):
    result = []
    start, end = [int(it) for it in range_str.split("-")]

    for val in range(start, end + 1):
        result.append(str(val))
    return result


total = 0

for range_str in data:
    for id_str in enumerate_all_ids(range_str):
        if is_invalid(id_str):
            total += int(id_str)

submit(total)
