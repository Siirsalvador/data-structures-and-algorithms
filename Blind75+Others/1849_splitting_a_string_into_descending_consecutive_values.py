class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(i, prev):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                cur = int(s[i:j + 1])
                if cur + 1 == prev and dfs(j + 1, cur):
                    return True

        for i in range(len(s)):
            if i == len(s) - 1:
                break
            cur = int(s[:i + 1])
            if dfs(i + 1, cur):
                return True
        return False
