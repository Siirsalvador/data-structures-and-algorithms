from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in num_set:
                cur = 1
                while num + cur in num_set:
                    cur += 1
                res = max(cur, res)

        return res
