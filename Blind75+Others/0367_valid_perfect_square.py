class Solution:
    def isPerfectSquareBinary(self, num: int) -> bool:
        if num == 1:
            return True

        low = 1
        high = num / 2

        while low <= high:
            mid = (low + high) / 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def isPerfectSquare(self, num: int) -> bool:
        val = 0
        i = 1
        while val < num:
            val = i * i
            if val == num:
                return True
            i += 1

        return False

    # expected to exceed time limit but apparently better than 73.40% of python submissions :)
