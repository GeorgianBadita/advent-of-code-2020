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


def find_sub_seq_sum(nums: List[int], preamble_size: int) -> int:
    preamble_size += 1
    wrong_index = preamble_size
    for i in range(preamble_size, len(nums)):
        if not two_sum(nums, i - preamble_size, i, nums[i]):
            wrong_index = i

    start, end = 0, 0
    sum_ = 0
    target = nums[wrong_index]
    while end < wrong_index:
        if sum_ < target:
            sum_ += nums[end]
            end += 1
        elif sum_ > target:
            sum_ -= nums[start]
            start += 1
        else:
            return min(nums[start + 1 : end + 1]) + max(nums[start + 1 : end + 1])


in_file = "day9/in-day-9.txt"
nums = read_data(in_file)
preamble_size = 25

print(find_sub_seq_sum(nums, preamble_size))