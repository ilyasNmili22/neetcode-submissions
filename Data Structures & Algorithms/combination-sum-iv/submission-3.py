from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(summ):
            if summ == target:
                return 1
            if summ > target:
                return 0
            if summ in memo:
                return memo[summ]
            
            total = 0
            for num in nums:
                total += dfs(summ + num)
            
            memo[summ] = total
            return total
        
        return dfs(0)
