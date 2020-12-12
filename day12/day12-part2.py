from typing import List, Tuple, Union


def read_input(in_file: str) -> List[Tuple[str, str]]:

    with open(in_file, "r") as f:
        return [(line[0].strip(), line[1:].strip()) for line in f.readlines()]


def apply_waypoint_rotation(current_pos: Tuple[int, int], new_direction: Tuple[str, str]) -> Tuple[str, str]:
    direction, degree = new_direction
    if direction == "R":
        degree = 360 - int(degree)
    else:
        degree = int(degree)

    if degree == 0 or degree == 360:
        return current_pos

    x, y = tuple(current_pos)
    if degree == 90:
        return y, -x
    if degree == 180:
        return -x, -y
    if degree == 270:
        return -y, x


def apply_ship_operation(
    current_ship: Tuple[int, int], current_waypoint: Tuple[int, int], op: Tuple[str, str]
) -> Tuple[int, int]:

    x_ship, y_ship = tuple(current_ship)

    x_way, y_way = tuple(current_waypoint)

    op_name, arg = op

    x_ship += int(arg) * x_way
    y_ship += int(arg) * y_way

    return (x_ship, y_ship)


def solve(ops: List[Tuple[str, str]]) -> int:
    current_ship_pos = (0, 0)
    current_waypoint_pos = (1, 10)

    for op in ops:
        op_name, arg = op
        if op_name == "F":
            current_ship_pos = apply_ship_operation(current_ship_pos, current_waypoint_pos, op)
        elif op_name == "L" or op_name == "R":
            current_waypoint_pos = apply_waypoint_rotation(current_waypoint_pos, op)
        elif op_name == "N":
            current_waypoint_pos = (current_waypoint_pos[0] + int(arg), current_waypoint_pos[1])
        elif op_name == "S":
            current_waypoint_pos = (current_waypoint_pos[0] - int(arg), current_waypoint_pos[1])
        elif op_name == "E":
            current_waypoint_pos = (current_waypoint_pos[0], current_waypoint_pos[1] + int(arg))
        elif op_name == "W":
            current_waypoint_pos = (current_waypoint_pos[0], current_waypoint_pos[1] - int(arg))

    print(current_ship_pos)
    return abs(current_ship_pos[0]) + abs(current_ship_pos[1])


in_file = "day12/in-day12.txt"

directions = read_input(in_file)
print(solve(directions))
