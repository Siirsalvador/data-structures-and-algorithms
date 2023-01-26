class Solution:
    def search(self, nums: list[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                res = m
                break

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:  # left sorted half -- target before pivot
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:  # right sorted half -- target after pivot
                    r = m - 1
                else:
                    l = m + 1
        return res
