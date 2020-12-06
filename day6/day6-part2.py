from typing import List
from functools import reduce


def read_groups(in_file: str) -> List[List[str]]:
    groups = []

    with open(in_file, "r") as f:
        current_group = []
        for line in f.readlines():
            if line == "\n":
                groups.append(current_group)
                current_group = []
            else:
                current_group.append(line.strip())

        groups.append(current_group)
        return groups


def count_yes_answered_by_all(groups: List[List[str]]) -> int:
    result = 0
    for group in groups:
        cnt_ans = [0] * 26
        for answer_pers in group:
            for answer in answer_pers:
                cnt_ans[ord(answer) - ord("a")] += 1
        for i in range(26):
            if cnt_ans[i] > 0 and cnt_ans[i] == len(group):
                result += 1
    return result


in_file = "day6/in-day-6.txt"

groups = read_groups(in_file)
print(count_yes_answered_by_all(groups))