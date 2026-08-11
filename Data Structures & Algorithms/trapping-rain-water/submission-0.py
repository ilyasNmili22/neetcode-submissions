class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        s = 0
        mn = 0
        while (l < r ):
            if height[l] < height[r]:
                #kamlin l
                mn = max(mn, height[l])
                if mn > height[l]:
                    s += (mn - height[l])
                l += 1
            elif height[l] > height[r]:
                #kamlin r
                mn = max(mn, height[r])
                if mn > height[r]:
                    s += (mn - height[r])
                r -= 1
            else:
                #kamlin l
                mn = max(mn, height[r])
                if mn > height[l]:
                    s += 2 * (mn - height[l])
                l += 1
                r -= 1
        #cas mzl ma7sbt w7da
        if l == r and height[l] < mn:
            s += (mn - height[l]) 
        return s