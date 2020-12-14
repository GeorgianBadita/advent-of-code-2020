from typing import List, Dict, Union


def read_input(in_file: str) -> Union[List[tuple], List[tuple]]:
    masks = []
    mem_ops = []
    with open(in_file, "r") as f:
        lines = f.readlines()
        current_mask = lines[0].split(" ")[-1].strip()
        mem_ops_for_mask = 0
        for line in lines[1:]:
            if "mask" in line:
                masks.append((current_mask, mem_ops_for_mask))
                current_mask = line.split(" ")[-1].strip()
                mem_ops_for_mask = 0
                continue
            else:
                mem_ops.append((int(line[line.index("[") + 1 : line.index("]")]), int(line.split(" ")[-1].strip())))
            mem_ops_for_mask += 1
    masks.append((current_mask, mem_ops_for_mask))
    return masks, mem_ops


def apply_mask(mask: str, current_number: int):

    for i in range(len(mask) - 1, -1, -1):
        current_bit = len(mask) - i - 1
        if mask[i] == "X":
            continue
        elif mask[i] == "1":
            current_number |= 1 << current_bit
        else:
            current_number &= ~(1 << current_bit)
    return current_number


def apply_mem_ops(masks: List[tuple], mem_ops: List[tuple]) -> int:
    mem_state = {}
    current_mask_index = 0
    current_mask, cnt = masks[current_mask_index]
    for mem_addr, mem_value in mem_ops:
        if cnt == 0:
            current_mask_index += 1
            current_mask, cnt = masks[current_mask_index]
        mem_state[mem_addr] = apply_mask(current_mask, mem_value)
        cnt -= 1
    return sum(mem_state.values())


in_file = "day14/in-day-14.txt"
masks, mem_ops = read_input(in_file)

print(apply_mem_ops(masks, mem_ops))