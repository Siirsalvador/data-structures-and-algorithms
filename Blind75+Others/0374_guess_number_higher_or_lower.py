# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            hint = self.guess(m)
            if hint == 0:
                return m
            elif hint > 0:
                l = m + 1
            elif hint < 0:
                r = m - 1
        return m + 1

    def guess(self, num):
        return 0
