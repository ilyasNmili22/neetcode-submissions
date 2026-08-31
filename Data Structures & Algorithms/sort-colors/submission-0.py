class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            indx_min = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[indx_min]:
                    indx_min = j
            nums[indx_min], nums[i] = nums[i], nums[indx_min]
            