import math
from typing import List


class Solution:
    def max_profit(self, closing_prices: List[int]) -> int:
        """
        Returns the maximum profit possible, given an array
        of closing prices over multiple days.
        :param closing_prices: List of integer closing prices.
        :return: Maximum profit possible.
        """
        cur_min = math.inf
        profit = 0
        for i in closing_prices:
            if i < cur_min:
                cur_min = i
            if i > cur_min:
                profit += i - cur_min
            cur_min = i

        return profit
