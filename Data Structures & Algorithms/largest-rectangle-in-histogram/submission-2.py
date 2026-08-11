class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while (stack and heights[i] <= stack[-1][0]):
                h, start = stack.pop()
                mx = max(mx, (i - start) * h)
            #print(stack)
            mx = max(mx, heights[i] * (i + 1 - start))    
            stack.append((heights[i], start))
            #print(heights[i], start)
        print(stack)
        
        for h, s in stack[:-1]:
            mx = max(mx, (len(heights)- s) * h)

        return mx