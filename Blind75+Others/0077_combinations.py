class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        candidates = [i for i in range(1, n + 1)]

        def dfs(cur_pos, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if cur_pos >= len(candidates) or len(cur) > k:
                return

            cur.append(candidates[cur_pos])
            dfs(cur_pos + 1, cur)

            cur.pop()
            dfs(cur_pos + 1, cur)

        dfs(0, [])
        return res
