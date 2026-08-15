class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new = [0] * len(nums)
        for x in nums:
            if x > 0 and x <= len(nums):
                new[x - 1] = 1
        for i in range(len(nums)):
            if not new[i]:
                return i + 1
        return len(nums) + 1



"""
O(n) in space, Not the best
"""