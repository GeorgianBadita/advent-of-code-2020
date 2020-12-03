from typing import List, Tuple, Optional

in_file = "day1/in-day-1.txt"


def read_input(in_file: str) -> List[int]:
    with open(in_file, "r") as f:
        lines = f.readlines()
        return [int(line.strip()) for line in lines]


def find_with_sum(nums: List[int], target: int) -> Optional[Tuple]:
    nums = sorted(nums)
    for i in range(len(nums)):
        new_target = target - nums[i]
        first = i + 1
        last = len(nums) - 1
        while first < last:
            if nums[first] + nums[last] == new_target and first != last != i:
                return (nums[first], nums[last], nums[i])
            if nums[first] + nums[last] > new_target:
                last -= 1
            else:
                first += 1
    return None


nums = read_input(in_file)
target = 2020
result = find_with_sum(nums, target)

if result:
    print(result[0] * result[1] * result[2])
else:
    raise IOError(f"No numbers found with sum: {target}")
