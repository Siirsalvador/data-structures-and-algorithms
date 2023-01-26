class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
