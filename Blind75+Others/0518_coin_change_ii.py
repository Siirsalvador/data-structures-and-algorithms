from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # time and space = O(amount * len(coins))
        # dp = [[0] * (amount + 1) for _ in range(len(coins))]
        # for i in range(len(coins)):
        #     dp[i][0] = 1

        # for cur_amount in range(1, amount + 1):
        #     for i in range(len(coins) - 1, -1, -1):
        #         if i + 1 < len(coins):
        #             dp[i][cur_amount] = dp[i + 1][cur_amount]
        #         if cur_amount - coins[i] in range(0, amount + 1):
        #             dp[i][cur_amount] += dp[i][cur_amount - coins[i]]
        # return dp[0][amount]
        ################################
        # time = O(amount * len(coins))
        # space = O(amount)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            new_dp = [0] * (amount + 1)
            new_dp[0] = 1
            for cur_amount in range(1, amount + 1):
                new_dp[cur_amount] = dp[cur_amount]
                if cur_amount - coins[i] in range(0, amount + 1):
                    new_dp[cur_amount] += new_dp[cur_amount - coins[i]]
            dp = new_dp
        return dp[amount]
