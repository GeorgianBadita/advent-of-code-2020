from typing import List
from functools import reduce


def read_groups(in_file: str) -> List[List[str]]:
    groups = []

    with open(in_file, "r") as f:
        current_group = ""
        for line in f.readlines():
            if line == "\n":
                groups.append(current_group)
                current_group = ""
            else:
                current_group += line.strip()

        groups.append(current_group)
        return groups


def count_yes_answered(groups: List[List[str]]) -> int:
    return reduce(lambda x, y: x + len(set(y)), groups, 0)


in_file = "day6/in-day-6.txt"

groups = read_groups(in_file)
print(count_yes_answered(groups))