class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        s = 0
        ans = float('inf')
        while (r < len(nums)):
            s += nums[r]
            while (l <= r and s >= target):
                print(s, l, r)
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1
            
            r += 1
        return ans if ans != float('inf') else 0
            


"""
nums = [2,1,5,1,5,3]

l = 0 r = 4
2, 3, 8, 9, 14 Done 5
l = 1, r = 4
14 - 2 = 12 Done 4

l = 2, r = 4
12 - 1 = 11 Done 3

l = 3, r = 4
11 - 5 = 6 No

l = 3, r = 5
6 + 3 = 9 No

"""