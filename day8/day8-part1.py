from typing import List


def read_input(in_file: str) -> List[str]:
    with open(in_file, "r") as f:
        return [
            str(index) + " " + line.strip() for index, line in enumerate(f.readlines())
        ]


def solve_for_infinite_loop(instructions: List[str]) -> int:
    current_instruction_index = 0
    accumulator = 0
    instructions_covered = set()

    infinite_loop = False
    while not infinite_loop:
        current_instruction = instructions[current_instruction_index]
        instruction_index, instruction, param = current_instruction.split(" ")
        if instruction_index in instructions_covered:
            infinite_loop = True
            continue
        instructions_covered.add(instruction_index)
        if instruction == "acc":
            accumulator += int(param)
            current_instruction_index += 1
        elif instruction == "jmp":
            current_instruction_index += int(param)
        else:
            current_instruction_index += 1
    return accumulator


in_file = "day8/in-day-8.txt"

instructions = read_input(in_file)

print(solve_for_infinite_loop(instructions))