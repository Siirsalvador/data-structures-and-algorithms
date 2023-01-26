class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numsSet = {num for num in nums}

        def dfs(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return res if res not in nums else None

            res = dfs(i + 1, cur)
            if res: return res
            cur[i] = "1"
            res = dfs(i + 1, cur)
            if res: return res

        return dfs(0, ["0" for n in nums])
