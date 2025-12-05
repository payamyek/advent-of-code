import functools
from aocd import data, submit


data = data.split()

PICKS = 12


@functools.cache
def fn(s: str, t: int):
    if len(s) == t:
        return s
    elif t == 1:
        return max(s)
    elif t > 2:
        return max(s[0] + fn(s[1:], t - 1), fn(s[1:], t))
    elif t == 2 and s[-1] == max(s):
        return max(s[0:-1]) + s[-1]
    elif t == 2:
        max_val = max(s)
        max_index = s.index(max_val)
        return max_val + max(s[max_index + 1 :])

    return s


total = 0

for bank in data:
    total += int(fn(bank, PICKS))


submit(total)
