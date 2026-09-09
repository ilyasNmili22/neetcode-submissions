from functools import cache
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache  #Need to understand behind the scences
        def dfs(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            ways = 0
            for num in nums:
                ways += dfs(remaining - num)
            return ways

        return dfs(target)