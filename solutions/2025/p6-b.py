from aocd import data, submit

ADD = "+"
MULTIPLY = "*"


data = data.split("\n")
WIDTH = max(len(row) for row in data)

data = [list(row.ljust(WIDTH)) for row in data]


def generate_sequence():
    sequence = []

    for i in range(WIDTH - 1, -1, -1):
        num = ""
        for j in range(len(data)):
            num += data[j][i]

        if ADD in num:
            num, _ = num.split(ADD)
            sequence.append(num.strip())
            sequence.append(ADD)
        elif MULTIPLY in num:
            num, _ = num.split(MULTIPLY)
            sequence.append(num.strip())
            sequence.append(MULTIPLY)
        else:
            sequence.append(num.strip())
    return [item for item in sequence if len(item)]


def solve():
    sequence = generate_sequence()

    accumulator = 0
    active_operator = ADD
    total = 0

    for item in sequence[::-1]:
        if item == ADD:
            total += accumulator
            # print(accumulator)
            accumulator = 0
            active_operator = ADD
        elif item == MULTIPLY:
            total += accumulator
            # print(accumulator)
            accumulator = 1
            active_operator = MULTIPLY
        elif active_operator == ADD:
            accumulator += int(item)
        else:
            accumulator *= int(item)
    total += accumulator
    return total


submit(solve())
