from typing import List


def read_data(in_file: str) -> List[int]:
    with open(in_file, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


def two_sum(nums: List[int], start, end, target) -> True:
    sums = {}
    for i in range(start, end):
        if target - nums[i] in sums:
            return True
        sums[nums[i]] = i
    return False


def find_first_wrong(nums: List[int], preamble_size: int) -> int:
    preamble_size += 1
    for i in range(preamble_size, len(nums)):
        if not two_sum(nums, i - preamble_size, i, nums[i]):
            return nums[i]
    return None


in_file = "day9/in-day-9.txt"
nums = read_data(in_file)
preamble_size = 25

print(find_first_wrong(nums, preamble_size))