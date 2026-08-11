class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = [1] + [0] * target

        for x in nums:
            for i in range(target, -1, -1):
                if dp[i] and x + i <= target:
                    dp[x + i] = 1
        #print(dp)
        return dp[-1] == 1