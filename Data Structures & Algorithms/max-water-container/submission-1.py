class Solution:
    def maxArea(self, heights):
        l , r = 0, len(heights) - 1
        mx = 0
        while (l < r):
            area = min(heights[l], heights[r]) * (r - l)
            mx = max(mx, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return mx