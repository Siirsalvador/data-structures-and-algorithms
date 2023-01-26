from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        wordDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i, soFar):
            if i == len(digits):
                res.append(soFar)
                return
            for c in wordDict[digits[i]]:
                dfs(i + 1, soFar + c)

        if digits:
            dfs(0, "")
        return res
