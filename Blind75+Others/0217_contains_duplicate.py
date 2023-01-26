from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_map = {}
        for i in range(len(nums)):
            if nums[i] in dup_map:
                return True
            else:
                dup_map[nums[i]] = True
        return False
