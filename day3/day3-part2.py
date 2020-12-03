from typing import List, Union
from functools import reduce


def read_input(in_file) -> List[str]:

    with open(in_file, "r") as f:
        return [line.strip() for line in f.readlines()]

    return []


def solve_for_slope(forest_map: List[str], slope: Union[int, int]):

    current_row = 0
    current_col = 0
    width = len(forest_map[0])
    right, down = slope
    cnt_trees = 0

    while current_row < len(forest_map):
        current_row += down
        current_col = (current_col + right) % width
        if (
            current_row < len(forest_map)
            and forest_map[current_row][current_col] == "#"
        ):
            cnt_trees += 1
    return cnt_trees


in_file = "day3/in-day-3.txt"
forest_map = read_input(in_file)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(
    reduce(
        lambda x, y: x * y, [solve_for_slope(forest_map, slope) for slope in slopes], 1
    )
)
