from typing import List
from functools import reduce

mapping = {"F": 0, "B": 1, "L": 0, "R": 1}


def read_input(in_file: str) -> List[str]:
    try:
        f_desc = open(in_file, "r")
        return [line.replace("\n", "") for line in f_desc.readlines()]
    except IOError:
        f_desc.close()
        return []


def compute_id(seat_desc: str) -> int:
    seat_id = 0
    for i in range(len(seat_desc) - 3):
        seat_id += mapping[seat_desc[i]] * (2 ** (len(seat_desc) - 4 - i))
    seat_id *= 8

    for i in range(3):
        seat_id += mapping[seat_desc[i + len(seat_desc) - 3]] * (2 ** (2 - i))
    return seat_id


in_file = "day5/in-day-5.txt"
seats = read_input(in_file)

sorted_seats_ids = sorted([compute_id(x) for x in seats])

for i in range(len(sorted_seats_ids) - 1):
    if sorted_seats_ids[i + 1] - sorted_seats_ids[i] != 1:
        print(sorted_seats_ids[i] + 1)
        break
