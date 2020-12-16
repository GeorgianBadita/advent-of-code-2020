from typing import Dict, List, Tuple


def read_input(in_file: str) -> Tuple[Dict[str, List[tuple]], List[List[int]]]:
    with open(in_file, "r") as f:
        lines = f.readlines()
        i = 0
        ranges_dict = {}
        while lines[i] != "\n":
            key, ranges = lines[i].split(":")
            rngs = ranges.split(" or ")
            field_rngs = []
            for rng in rngs:
                a, b = int(rng.split("-")[0].strip()), int(rng.split("-")[1].strip())
                field_rngs.append((a, b))
            ranges_dict[key] = field_rngs
            i += 1
        nearby_tickets_index = i + 5
        tickets = []
        while nearby_tickets_index < len(lines):
            tickets.append([int(x) for x in lines[nearby_tickets_index].split(",")])
            nearby_tickets_index += 1
    return ranges_dict, tickets


def number_in_at_least_one_range(number: int, ranges: Dict[str, List[int]]) -> bool:
    for value in ranges.values():
        for a, b in value:
            if a <= number <= b:
                return True
    return False


def solve(tickets: List[List[int]], ranges: Dict[str, List[tuple]]):
    wrong_sum = 0
    for ticket in tickets:
        for ticket_value in ticket:
            wrong_sum += ticket_value if not number_in_at_least_one_range(ticket_value, ranges) else 0
    return wrong_sum


in_file = "day16/in-day-16.txt"

ranges, tickets = read_input(in_file)

print(solve(tickets, ranges))