class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in nums:
            i = abs(x)
            if nums[i] < 0:
                return i
            nums[i] *= -1
        return -1