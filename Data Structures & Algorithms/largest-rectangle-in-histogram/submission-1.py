class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx = 0
        for i in range(len(heights)):
            r = i + 1
            while (r < len(heights) and heights[r] >= heights[i]):
                r += 1
            l = i - 1
            while (l >= 0 and heights[l] >= heights[i]):
                l -= 1
            mx = max(mx, (r - l - 1) * heights[i])
            #print(i, l, r)
            #i+1-i+1
        return mx
#[2,1,2]
#l = 0, r = 3