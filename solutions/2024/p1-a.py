from aocd import data

data = data.split()

left_list = sorted(
    [int(location_id) for index, location_id in enumerate(data) if index % 2 == 0]
)

right_list = sorted(
    [int(location_id) for index, location_id in enumerate(data) if index % 2 == 1]
)

total_distance = 0

for left_element, right_element in zip(left_list, right_list):
    total_distance += abs(left_element - right_element)

print(total_distance)
