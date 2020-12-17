from typing import Dict, List


def read_input(in_file: str) -> Dict[tuple, str]:
    pocket = {}
    with open(in_file, "r") as f:
        for x, line in enumerate(f.readlines()):
            for y, state in enumerate(line.strip()):
                if state == "#":
                    pocket[(x, y, 0)] = "#"
    return pocket


def get_adj(x: int, y: int, z: int) -> List[tuple]:
    lst = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == j == k == 0:
                    continue
                lst.append((x + i, y + j, z + k))
    return lst


def get_coords(pocket: Dict[tuple, str]):
    x = [x for x, _, __ in pocket.keys()]
    y = [y for _, y, __ in pocket.keys()]
    z = [z for _, __, z in pocket.keys()]
    return min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1, min(z) - 1, max(z) + 1


def get_num_active(x: int, y: int, z: int, pocket: Dict[tuple, str]):
    actives = 0
    for adj in get_adj(x, y, z):
        actives += 1 if pocket.get(adj, ".") == "#" else 0

    return actives


def solve(pocket: Dict[tuple, str]) -> int:
    for _ in range(6):
        new_pocket = {}
        min_x, max_x, min_y, max_y, min_z, max_z = get_coords(pocket)
        for z in range(min_z - 1, max_z + 1):
            for x in range(min_x - 1, max_x + 1):
                for y in range(min_y - 1, max_y + 1):
                    num_active = get_num_active(x, y, z, pocket)
                    if pocket.get((x, y, z), ".") == "#" and (num_active == 2 or num_active == 3):
                        new_pocket[(x, y, z)] = "#"
                    elif pocket.get((x, y, z), ".") == "." and num_active == 3:
                        new_pocket[(x, y, z)] = "#"
        pocket = new_pocket.copy()
    return len(pocket.values())


in_file = "day17/in-day-17.txt"

pocket = read_input(in_file)

print(solve(pocket))
