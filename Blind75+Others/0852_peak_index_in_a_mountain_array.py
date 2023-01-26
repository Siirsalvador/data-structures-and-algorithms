class Solution:
    def peakIndexInMountainArray(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
                return m

            if nums[m] < nums[m - 1]:
                r = m
            elif nums[m] < nums[m + 1]:
                l = m
