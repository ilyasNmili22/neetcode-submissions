class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = curr = nums[0]
        for i in range(1, len(nums)):
            curr += nums[i]
            if curr > maxs:
                maxs = curr
            if curr < 0:
                curr = 0
        return max(maxs, nums[-1])