class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_min = cur_max = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                cur_min = cur_max = 1
            temp = cur_min * nums[i]
            cur_min = min(cur_min * nums[i], nums[i], cur_max * nums[i])
            cur_max = max(cur_max * nums[i], nums[i], temp)
            res = max(res, cur_max)

        return res
