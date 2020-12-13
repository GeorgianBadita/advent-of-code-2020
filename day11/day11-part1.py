from typing import List


def read_input(in_file: str) -> List[str]:
    with open(in_file, "r") as f:
        return [[char for char in line.strip()] for line in f.readlines()]


def valid_coords(x: int, y: int, seats_map: List[str]) -> bool:
    return x >= 0 and x < len(seats_map) and y >= 0 and y < len(seats_map[0])


def until_chaos_stabilizes(seats_map: List[str]) -> int:
    chaoos_stabilized = False
    dx = [1, -1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    while not chaoos_stabilized:
        chaoos_stabilized = True
        changes = []
        for row in range(len(seats_map)):
            for col in range(len(seats_map[0])):
                if seats_map[row][col] == "L":
                    occupied = False
                    for i in range(len(dx)):
                        adj_row, adj_col = row + dx[i], col + dy[i]
                        if (
                            valid_coords(adj_row, adj_col, seats_map)
                            and seats_map[adj_row][adj_col] == "#"
                        ):
                            occupied = True
                            break
                    if not occupied:
                        changes.append((row, col, "#"))
                elif seats_map[row][col] == "#":
                    num_occupied_adj = 0
                    for i in range(len(dx)):
                        adj_row, adj_col = row + dx[i], col + dy[i]
                        if (
                            valid_coords(adj_row, adj_col, seats_map)
                            and seats_map[adj_row][adj_col] == "#"
                        ):
                            num_occupied_adj += 1
                    if num_occupied_adj >= 4:
                        changes.append((row, col, "L"))
        if changes:
            chaoos_stabilized = False
            for change in changes:
                row, col, seat_type = change
                seats_map[row][col] = seat_type

    return sum([line.count("#") for line in seats_map])


in_file = "day11/in-day-11.txt"

seats_map = read_input(in_file)

print(until_chaos_stabilizes(seats_map))
