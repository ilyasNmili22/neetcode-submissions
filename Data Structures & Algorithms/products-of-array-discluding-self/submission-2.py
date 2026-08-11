class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        p = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                p *= nums[i]
        ret = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0 and zeros == 0:
                ret[i] = p // nums[i]
            elif nums[i] == 0 and zeros == 1:
                ret[i] = p
        return ret
