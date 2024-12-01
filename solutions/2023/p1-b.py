from aocd import data, submit

word_to_digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_digit_character(input: str, reverse=False) -> str:
    for index, char in enumerate(input):
        if char.isdigit():
            return char
        for word in word_to_digit_map:
            if not reverse and input[index:].startswith(word):
                return word_to_digit_map[word]
            elif reverse and input[index:].startswith(word[::-1]):
                return word_to_digit_map[word]

    return None


def get_calibration_value(input: str) -> int:
    leftmost_digit = get_first_digit_character(input)
    rightmost_digit = get_first_digit_character(input[::-1], reverse=True)
    return int(leftmost_digit + rightmost_digit)


data = data.splitlines()
result = sum([get_calibration_value(input) for input in data])

submit(result)
