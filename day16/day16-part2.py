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
        tickets = [[int(x) for x in lines[i + 2].split(",")]]
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


def get_good_tickets(tickets: List[List[int]], ranges: Dict[str, List[tuple]]):
    good_tickets = []
    for ticket in tickets:
        should_discard = False
        for ticket_value in ticket:
            if not number_in_at_least_one_range(ticket_value, ranges):
                should_discard = True
                break
        if not should_discard:
            good_tickets.append(ticket)
    return good_tickets


def assign_cols_for_departures(tickets: List[List[int]], ranges: Dict[str, List[tuple]]):
    assigned = {val: [] for val in ranges.keys()}

    for key in ranges.keys():
        range_for_key = ranges[key]

        for col in range(len(tickets[0])):
            is_col_for_key = True

            for line in range(len(tickets)):
                curr_val = tickets[line][col]
                matches = False
                for a, b in range_for_key:
                    if a <= curr_val <= b:
                        matches = True
                        break

                if not matches:
                    is_col_for_key = False
                    break
            if is_col_for_key:
                assigned[key].append(col)

    return assigned


in_file = "day16/in-day-16.txt"

ranges, tickets = read_input(in_file)
init_ticket = tickets[0]

good_tickets = get_good_tickets(tickets, ranges)

assigned = assign_cols_for_departures(good_tickets, ranges)
keys_list = list(assigned.keys())
values_list = list(assigned.values())


i = 0
while i < len(keys_list):
    keys_list = sorted(keys_list, key=lambda elem: len(assigned[elem]))
    values_list = sorted(values_list, key=lambda elem: len(elem))
    current_elem = values_list[i][-1]
    for lst in values_list:
        if len(lst) != 1 and current_elem in lst:
            lst.remove(current_elem)
    i += 1


prod = 1
for key, value in assigned.items():
    if "departure" in key:
        prod *= init_ticket[value[-1]]

print(prod)
