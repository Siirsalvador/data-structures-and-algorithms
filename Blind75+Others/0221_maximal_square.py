from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}

        def dfs(i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            down = dfs(i + 1, j)
            right = dfs(i, j + 1)
            diag = dfs(i + 1, j + 1)
            dp[(i, j)] = 0
            if matrix[i][j] == "1":
                dp[(i, j)] = 1 + min(down, right, diag)
            return dp[(i, j)]

        dfs(0, 0)
        return max(dp.values()) ** 2
