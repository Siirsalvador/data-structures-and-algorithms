from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(vals):
            store1 = store2 = 0

            for n in vals:
                temp = max(n + store1, store2)
                store1 = store2
                store2 = temp
            return store2

        return max(nums[0], robber(nums[1:]), robber(nums[:-1]))
