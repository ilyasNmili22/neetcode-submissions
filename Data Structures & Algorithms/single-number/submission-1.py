class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for x in nums:
            r  = r ^ x
        return r