import re
from aocd import data, submit


INSTRUCTION_DO = "DO"
INSTRUCTION_DONT = "DONT"
INSTRUCTION_MUL = "MUL"

all_donts = [
    (m.start(0), m.end(0), INSTRUCTION_DO) for m in re.finditer(r"do\(\)", data)
]

all_dos = [
    (m.start(0), m.end(0), INSTRUCTION_DONT) for m in re.finditer(r"don't\(\)", data)
]

all_muls = [
    (m.span(1), m.span(2), INSTRUCTION_MUL)
    for m in re.finditer(r"mul\((\d+),(\d+)\)", data)
]

sorted_list = sorted(
    all_donts + all_dos + all_muls,
    key=lambda x: x[0][0] if x[2] == INSTRUCTION_MUL else x[0],
)


active = True
sum = 0

for instruction in sorted_list:
    if active and instruction[2] == INSTRUCTION_MUL:
        first_start, first_end = instruction[0]
        second_start, second_end = instruction[1]
        sum = sum + int(data[first_start:first_end]) * int(
            data[second_start:second_end]
        )
    elif instruction[2] == INSTRUCTION_DONT:
        active = False
    elif instruction[2] == INSTRUCTION_DO:
        active = True

submit(sum)
