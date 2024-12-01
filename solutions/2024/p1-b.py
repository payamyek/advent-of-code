from aocd import data

data = data.split()

left_list = sorted(
    [int(location_id) for index, location_id in enumerate(data) if index % 2 == 0]
)

right_list = sorted(
    [int(location_id) for index, location_id in enumerate(data) if index % 2 == 1]
)

total = 0

for left_element in left_list:
    total += right_list.count(left_element) * left_element

print(total)
