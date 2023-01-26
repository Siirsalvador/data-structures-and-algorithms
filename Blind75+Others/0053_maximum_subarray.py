class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0

        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            max_sub = max(max_sub, cur_sum)
        return max_sub
