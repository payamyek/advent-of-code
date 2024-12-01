from aocd import data, submit


def get_first_digit_character(input: str) -> str:
    for char in input:
        if char.isdigit():
            return char
    return None


def get_calibration_value(input: str) -> int:
    leftmost_digit = get_first_digit_character(input)
    rightmost_digit = get_first_digit_character(input[::-1])
    return int(leftmost_digit + rightmost_digit)


data = data.splitlines()
result = sum([get_calibration_value(input) for input in data])

submit(result)
