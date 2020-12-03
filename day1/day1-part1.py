from typing import List, Tuple, Optional

in_file = "day1/in-day-1.txt"


def read_input(in_file: str) -> List[int]:
    with open(in_file, "r") as f:
        lines = f.readlines()
        return [int(line.strip()) for line in lines]


def find_with_sum(nums: List[int], target: int) -> Optional[Tuple]:
    seen_sums = set()
    for num in nums:
        if target - num in seen_sums:
            return (num, target - num)
        seen_sums.add(num)

    return None


nums = read_input(in_file)
target = 2020
result = find_with_sum(nums, target)

if result:
    print(result[0] * result[1])
else:
    raise IOError(f"No numbers found with sum: {target}")
