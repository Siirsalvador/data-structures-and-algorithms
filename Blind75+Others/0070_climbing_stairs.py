class Solution:
    def climbStairs(self, n: int) -> int:
        var_1 = 1
        var_2 = 1
        result = 1
        for i in range(n - 1):
            result = var_1 + var_2
            var_1 = var_2
            var_2 = result
        return result
