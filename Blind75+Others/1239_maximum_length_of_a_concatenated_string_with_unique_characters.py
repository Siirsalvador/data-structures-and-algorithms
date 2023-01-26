from collections import Counter
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_set = set()

        def overlap(s):
            c = Counter(char_set) + Counter(s)
            return max(c.values()) > 1

        def backtrack(pos):
            if pos == len(arr):
                return len(char_set)

            res = 0
            if not overlap(arr[pos]):
                for c in arr[pos]:
                    char_set.add(c)
                res = (backtrack(pos + 1))
                for c in arr[pos]:
                    char_set.remove(c)
            return max(res, backtrack(pos + 1))

        return backtrack(0)