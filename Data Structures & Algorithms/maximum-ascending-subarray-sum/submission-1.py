class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        mx = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                s += nums[i]     
                mx = max(s, mx)
            else:
                s = nums[i]
        return mx



"""
10 20 30 5 10 50
10
30
60
5
15
65
"""