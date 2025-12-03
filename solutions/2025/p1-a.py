from aocd import data, submit

LEFT = "L"
RIGHT = "R"

data = data.split()

# Dials -> 0..99
# R -> higher number
# L -> lower number

dial_pos = 50
count = 0

for rotation in data:
    direction = rotation[0]
    units = int(rotation[1:])

    if direction == RIGHT:
        dial_pos = (units + dial_pos) % 100
    else:
        dial_pos = (-units + dial_pos) % 100

    if dial_pos == 0:
        count += 1

submit(count)
