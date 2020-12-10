from typing import List


def read_input(in_file: str) -> List[int]:
    with open(in_file, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


def compute_num_of_corret_joltages(adapters: List[int]) -> int:
    adapters = sorted(adapters)

    correct_joltages = [0] * (1 + adapters[-1])
    correct_joltages[0] = 1
    for num in adapters:
        correct_joltages[num] = (
            correct_joltages[num - 3]
            + correct_joltages[num - 2]
            + correct_joltages[num - 1]
        )
    return correct_joltages[-1]


in_file = "day10/in-day-10.txt"

adapters = read_input(in_file)


print(compute_num_of_corret_joltages(adapters))
