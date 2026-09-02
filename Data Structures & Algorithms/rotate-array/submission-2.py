class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = []
        n = len(nums)
        k %= n
        for i in range(n):
            nums2.append(nums[i-k])
        for i in range(n):
            nums[i] = nums2[i]
        