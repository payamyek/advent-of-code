from aocd import data, submit


data = [it for it in data.split(",")]


def is_invalid(str_num: str):
    for chunk_size in range(1, (len(str_num) // 2) + 1):
        parts = []

        for i in range(0, len(str_num), chunk_size):
            part = str_num[i : i + chunk_size]
            parts.append(part)

        if any(p[0] == "0" for p in parts):
            continue

        if len(set(parts)) == 1:
            return True
    return False


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
