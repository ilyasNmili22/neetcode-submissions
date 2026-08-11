class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            mx = 1
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    mx = max(mx, dp[j] + 1)
            dp[i] = mx
        return max(dp)