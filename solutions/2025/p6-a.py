from aocd import data, submit

ADD = "+"
MULTIPLY = "*"

data = [row.strip().split() for row in data.split("\n")]


def solve():
    operators = data[-1]
    accumulator = [0 if op == ADD else 1 for op in operators]

    for row in data[:-1]:
        for index in range(len(row)):
            if operators[index] == ADD:
                accumulator[index] += int(row[index])
            else:
                accumulator[index] *= int(row[index])
    return sum(accumulator)


submit(solve())
