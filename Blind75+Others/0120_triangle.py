import math
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i + 1 >= len(triangle):
                return triangle[i][j]
            if j >= len(triangle[i]) or j < 0:
                return math.inf

            val = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
            memo[(i, j)] = val

            return memo[(i, j)]

        return dfs(0, 0)
