from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(pos, cur, total):
            if total == target:
                res.append(cur.copy())
            if total > target or pos >= len(candidates):
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(i + 1, cur, total + candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res
