from typing import List, Tuple, Optional


def read_input(in_file: str) -> List[str]:
    with open(in_file, "r") as f:
        return [
            str(index) + " " + line.strip() for index, line in enumerate(f.readlines())
        ]


def compute_sum(instructions: List[str]) -> Optional[int]:
    current_instruction_index = 0
    accumulator = 0
    instructions_covered = set()

    while current_instruction_index < len(instructions):
        current_instruction = instructions[current_instruction_index]
        instr_index, instruction, param = current_instruction.split(" ")
        if instr_index in instructions_covered:
            return None
        instructions_covered.add(instr_index)
        if instruction == "acc":
            accumulator += int(param)
            current_instruction_index += 1
        elif instruction == "jmp":
            current_instruction_index += int(param)
        else:
            current_instruction_index += 1
    return accumulator


def make_jmp_nop(instructions: List[str]) -> Optional[int]:
    jumps = [
        instruction
        for instruction in instructions
        if instruction.split(" ")[1] == "jmp"
    ]
    for jmp in jumps:
        local_instructions = instructions[:]
        index, _, param = jmp.split(" ")
        local_instructions[int(index)] = " ".join([index, "nop", param])
        acc_val = compute_sum(local_instructions)
        if acc_val:
            return acc_val


in_file = "day8/in-day-8.txt"

instructions = read_input(in_file)

change_jmp = make_jmp_nop(instructions)
if change_jmp:
    print(change_jmp)