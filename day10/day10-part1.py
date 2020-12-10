from typing import List


def read_input(in_file: str) -> List[int]:
    with open(in_file, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


def compute_voltages_differences(adapters: List[int]) -> int:

    adapters = sorted(adapters)
    one_jolts_diffs = 0
    three_jolts_diffs = 0
    if adapters[0] == 1:
        one_jolts_diffs += 1
    elif adapters[0] == 3:
        three_jolts_diffs += 1
    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            one_jolts_diffs += 1
        elif adapters[i + 1] - adapters[i] == 3:
            three_jolts_diffs += 1
    return three_jolts_diffs * one_jolts_diffs


in_file = "day10/in-day-10.txt"

adapters = read_input(in_file)
adapters.append(max(adapters) + 3)

print(compute_voltages_differences(adapters))
