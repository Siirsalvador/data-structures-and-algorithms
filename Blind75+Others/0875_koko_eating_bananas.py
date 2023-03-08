import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2
            t = 0
            for i in range(len(piles)):
                cur = piles[i]
                t += math.ceil(cur/m)
            if t > h:
                l = m + 1
            if t <= h:
                r = m

        return l