from typing import Dict, List


def read_input(in_file: str) -> Dict[tuple, str]:
    pocket = {}
    with open(in_file, "r") as f:
        for x, line in enumerate(f.readlines()):
            for y, state in enumerate(line.strip()):
                if state == "#":
                    pocket[(x, y, 0, 0)] = "#"
    return pocket


def get_adj(x: int, y: int, z: int, w: int) -> List[tuple]:
    lst = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i == j == k == l == 0:
                        continue
                    lst.append((x + i, y + j, z + k, l + w))
    return lst


def get_coords(pocket: Dict[tuple, str]):
    x = [x for x, a, b, c in pocket.keys()]
    y = [y for b, y, b, c in pocket.keys()]
    z = [z for a, b, z, c in pocket.keys()]
    w = [w for a, b, c, w in pocket.keys()]

    return min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1, min(z) - 1, max(z) + 1, min(w) - 1, max(w) + 1


def get_num_active(x: int, y: int, z: int, w: int, pocket: Dict[tuple, str]):
    actives = 0
    for adj in get_adj(x, y, z, w):
        actives += 1 if pocket.get(adj, ".") == "#" else 0

    return actives


def solve(pocket: Dict[tuple, str]) -> int:
    for _ in range(6):
        new_pocket = {}
        min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w = get_coords(pocket)
        for w in range(min_w - 1, max_w + 1):
            for z in range(min_z - 1, max_z + 1):
                for x in range(min_x - 1, max_x + 1):
                    for y in range(min_y - 1, max_y + 1):
                        num_active = get_num_active(x, y, z, w, pocket)
                        if pocket.get((x, y, z, w), ".") == "#" and (num_active == 2 or num_active == 3):
                            new_pocket[(x, y, z, w)] = "#"
                        elif pocket.get((x, y, z, w), ".") == "." and num_active == 3:
                            new_pocket[(x, y, z, w)] = "#"
        pocket = new_pocket.copy()
    return len(pocket.values())


in_file = "day17/in-day-17.txt"

pocket = read_input(in_file)

print(solve(pocket))
