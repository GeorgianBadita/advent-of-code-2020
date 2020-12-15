from typing import List


def read_input(in_file: str) -> List[int]:
    with open(in_file, "r") as f:
        line = f.readline()
        return [int(elem.strip()) for elem in line.split(",")]


def take_turns(numbers: List[int], n_th: int) -> int:
    occurances = {}
    for i in range(len(numbers)):
        if numbers[i] in occurances:
            occurances[numbers[i]].append(i + 1)
        else:
            occurances[numbers[i]] = [i + 1]

    last_occurance = 0
    current_turn = len(numbers) + 1
    while current_turn < n_th:
        if last_occurance not in occurances:
            occurances[last_occurance] = [current_turn]
            last_occurance = 0
        else:
            occurances[last_occurance].append(current_turn)
            last_occurance = occurances[last_occurance][-1] - occurances[last_occurance][-2]
        current_turn += 1
    return last_occurance


in_file = "day15/in-day-15.txt"

init_numbers = read_input(in_file)
print(take_turns(init_numbers, 2020))