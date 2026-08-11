class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mn = 1
        res = -float('inf')
        for x in nums:
            if x == 0:
                mx = mn = 1
                res = max(res, 0)
                continue
            t = mx
            mx = max(x, x * mn, x * mx)
            mn = min(x, x * mn, x * t)
            res = max(res, mx)
            #print(mx, mn, res)
        return res