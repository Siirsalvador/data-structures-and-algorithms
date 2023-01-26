class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            cur_area = (r - l) * min(height[r], height[l])
            max_area = max(cur_area, max_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area
