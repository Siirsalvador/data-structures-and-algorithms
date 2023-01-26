class Solution:
    def longestPalindrome(self, s: str) -> str:
        min_back = max_front = 0
        for i in range(0, len(s) - 1):
            back = front = i
            while back >= 0 and front < len(s) and s[back] == s[front]:
                if (front - back) > (max_front - min_back):
                    max_front = front
                    min_back = back
                back -= 1
                front += 1

            back = i
            front = i + 1
            while back >= 0 and front < len(s) and s[back] == s[front]:
                if (front - back) > (max_front - min_back):
                    max_front = front
                    min_back = back
                back -= 1
                front += 1

        return s[min_back:max_front + 1]
