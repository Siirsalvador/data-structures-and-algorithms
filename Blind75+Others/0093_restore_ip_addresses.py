from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return res

        def backtrack(pos, dots, curIP):
            if dots == 4 and pos == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return

            for i in range(pos, min(pos + 3, len(s))):
                if int(s[pos:i + 1]) < 256 and (pos == i or s[pos] != "0"):
                    backtrack(i + 1, dots + 1, curIP + s[pos:i + 1] + ".")

        backtrack(0, 0, "")
        return res
