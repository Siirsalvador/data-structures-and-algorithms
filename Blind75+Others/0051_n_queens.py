from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = set()
        rdiag = set()
        ldiag = set()

        board = [["."] * n for i in range(n)]
        res = []

        def solveQueens(c):
            if c == n:
                res.append(["".join(row) for row in board])
                return

            for r in range(n):
                if r in row or (r + c) in rdiag or (r - c) in ldiag:
                    continue

                row.add(r)
                rdiag.add(r + c)
                ldiag.add(r - c)
                board[r][c] = 'Q'

                solveQueens(c + 1)

                row.remove(r)
                rdiag.remove(r + c)
                ldiag.remove(r - c)
                board[r][c] = '.'

        solveQueens(0)
        return res
