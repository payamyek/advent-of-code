from aocd import data, submit

LEFT = "L"
RIGHT = "R"
DIALS = 100

data = data.split()
# data = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

# Dials -> 0..99
# R -> higher number
# L -> lower number
# Q? How many times does it past zero?

dial_pos = 50
count = 0

for rotation in data:
    direction = rotation[0]
    units = int(rotation[1:])

    count += abs((dial_pos + units) // DIALS)

    # print(abs((dial_pos + units) // DIALS))

    if direction == RIGHT:
        dial_pos = (units + dial_pos) % DIALS
    else:
        dial_pos = (-units + dial_pos) % DIALS

    # if dial_pos == 0:
    #     count += 1
    #     print("y0")
    # print()


submit(count)
