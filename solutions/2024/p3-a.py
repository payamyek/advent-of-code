from aocd import data, submit
import re


result = [(int(x), int(y)) for x, y in re.findall("mul\((\d+),(\d+)\)", data)]

result = sum([x * y for x, y in result])

submit(result)
