from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def existRecur(r, c, loc):
            if loc == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows
                    or c >= cols or word[loc] != board[r][c]
                    or (r, c) in path):
                return False

            path.add((r, c))
            res = (existRecur(r, c + 1, loc + 1) or
                   existRecur(r, c - 1, loc + 1) or
                   existRecur(r + 1, c, loc + 1) or
                   existRecur(r - 1, c, loc + 1))
            path.remove((r, c))

            return res

        for i in range(rows):
            for j in range(cols):
                if existRecur(i, j, 0):
                    return True

        return False
