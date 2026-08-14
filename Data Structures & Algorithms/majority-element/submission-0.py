class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mj = len(nums) // 2
        for x in nums:
            if nums.count(x) > mj:
                return x
        return -1