from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)

    def lengthOfLISBinarySearch(self, nums: List[int]) -> int:
        sub = []

        for i in nums:
            if len(sub) == 0 or sub[-1] < i:
                sub.append(i)
            else:
                idx = bisect_left(sub, i)

                sub[idx] = i
        return len(sub)
