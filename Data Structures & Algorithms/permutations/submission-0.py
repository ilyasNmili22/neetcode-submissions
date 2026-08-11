class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(nums, left, right):
            if left == right:
                ret.append(nums[:])
            for i in range(left, right + 1):
                nums[i], nums[left] = nums[left], nums[i]
                backtrack(nums, left + 1, right)
                nums[i], nums[left] = nums[left], nums[i]
        backtrack(nums, 0, len(nums) - 1)
        return ret