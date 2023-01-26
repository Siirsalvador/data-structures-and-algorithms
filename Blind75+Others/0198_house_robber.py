from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        store1 = store2 = 0

        for n in nums:
            temp = max(n + store1, store2)
            store1 = store2
            store2 = temp
        return store2
    