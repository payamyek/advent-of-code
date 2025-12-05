from aocd import data, submit

data = data.split()


def max_bank_voltage(bank: str) -> int:
    max_value = max(bank)
    max_index = bank.index(max_value)

    if max_index == len(bank) - 1:
        second_max_value = max(bank[:max_index])
        return int(second_max_value + max_value)
    else:
        second_max_value = max(bank[max_index + 1 :])
        return int(max_value + second_max_value)


total = 0

for bank in data:
    total += max_bank_voltage(bank)

submit(total)
