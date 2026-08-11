class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(nums, indx):
            if indx == len(nums):
                ret.append(nums[:])
            for i in range(indx, len(nums)):
                nums[i], nums[indx] = nums[indx], nums[i]
                backtrack(nums, indx + 1)
                nums[i], nums[indx] = nums[indx], nums[i]
        backtrack(nums,0)
        return ret