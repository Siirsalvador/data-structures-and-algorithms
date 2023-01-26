class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = set([i for i in range(len(nums) + 1)]).difference(set(nums))
        if len(res) < 1:
            return 0
        return res.pop()

    def missingNumberXOR(self, nums):
        result = 0
        for i in nums:
            result ^= i

        for i in range(len(nums) + 1):
            result ^= i

        return result
