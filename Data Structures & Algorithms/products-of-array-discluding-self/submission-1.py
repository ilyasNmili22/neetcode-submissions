class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                p *= nums[i]
            else:
                zeros += 1
        for i in range(len(nums)):
            if nums[i] != 0 and zeros == 0:
                nums[i] = p // nums[i]
            elif nums[i] != 0 and zeros >= 0:
                nums[i] = 0
            elif nums[i] == 0 and zeros == 1:
                nums[i] = p
        return nums
                
        return nums 