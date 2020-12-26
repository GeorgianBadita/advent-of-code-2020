def read_input(in_file: str) -> tuple:
    with open(in_file, "r") as f:
        lines = f.readlines()
        return int(lines[0].strip()), int(lines[1].strip())


def solve(card: int, door: int):
    curr = 0
    while pow(7, curr, 20201227) != card:
        curr += 1
    return pow(door, curr, 20201227)


in_file = "day25/in-day-25.txt"
card, door = read_input(in_file)

print(solve(card, door))