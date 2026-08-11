class Solution:
    def maxArea(self, heights):
        mx = min(heights[0], heights[1])
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                mx = max(mx, min(heights[i], heights[j]) * (j - i))
        return mx