class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for x in coins:
            if x <= amount:
                dp[x] = 1
        
        for i in range(1, amount + 1):
            mn = float('inf')
            for x in coins:
                if 0 <= i - x <= amount and dp[i - x] != -1:
                    mn = min(mn, dp[i - x])
            if mn != float('inf'):
                dp[i] = 1 + mn
            #print(i, dp[i])
        return dp[-1]