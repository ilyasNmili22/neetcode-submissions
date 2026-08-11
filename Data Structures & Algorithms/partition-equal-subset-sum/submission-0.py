class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = [1] + [0] * target

        for x in nums:
            change = []
            for i in range(target + 1):
                if dp[i] == 1 and x + i <= target:
                    change.append(x + i)
            for x in change:
                dp[x] = 1
        #print(dp)
        return dp[-1] == 1