from typing import List, Tuple, Union


def read_input(in_file: str) -> List[Tuple[str, str]]:

    with open(in_file, "r") as f:
        return [(line[0].strip(), line[1:].strip()) for line in f.readlines()]


def change_direction(current_direction: str, new_direction: Tuple[str, str]) -> str:
    direction, degree = new_direction
    if direction == "R":
        degree = 360 - int(degree)
    else:
        degree = int(degree)

    if degree == 0 or degree == 360:
        return current_direction

    if current_direction == "N":
        if degree == 90:
            return "W"
        elif degree == 180:
            return "S"
        elif degree == 270:
            return "E"
    if current_direction == "S":
        if degree == 90:
            return "E"
        elif degree == 180:
            return "N"
        elif degree == 270:
            return "W"
    if current_direction == "E":
        if degree == 90:
            return "N"
        if degree == 180:
            return "W"
        elif degree == 270:
            return "S"
    if current_direction == "W":
        if degree == 90:
            return "S"
        if degree == 180:
            return "E"
        elif degree == 270:
            return "N"
    raise Exception(f"Invalud input, current_direction-{current_direction}, new_direction-{new_direction}")


def apply_operation(current_pos: Tuple[str, int, int], op: Tuple[str, str]) -> Tuple[str, int, int]:
    op_name, arg = op
    current_dir, x, y = current_pos

    if op_name == "F":
        if current_dir == "N":
            x += int(arg)
        if current_dir == "S":
            x -= int(arg)
        if current_dir == "E":
            y += int(arg)
        if current_dir == "W":
            y -= int(arg)
    elif op_name == "L" or op_name == "R":
        current_dir = change_direction(current_dir, op)
    elif op_name == "N":
        x += int(arg)
    elif op_name == "S":
        x -= int(arg)
    elif op_name == "E":
        y += int(arg)
    elif op_name == "W":
        y -= int(arg)

    return current_dir, x, y


def solve(ops: List[Tuple[str, str]]) -> int:
    current_poistion = ("E", 0, 0)
    for op in ops:
        current_poistion = apply_operation(current_poistion, op)

    return abs(current_poistion[1]) + abs(current_poistion[2])


in_file = "day12/in-day12.txt"

directions = read_input(in_file)
print(solve(directions))
