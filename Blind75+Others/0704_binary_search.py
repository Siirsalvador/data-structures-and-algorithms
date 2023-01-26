class Solution:
    def search(self, nums: list[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                res = m
                break
            if nums[m] >= target:
                r = m - 1
            if nums[m] < target:
                l = m + 1
        return res
