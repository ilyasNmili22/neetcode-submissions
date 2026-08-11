class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left < right):
            med = (right + left) // 2
            if target > nums[med]:
                left = med + 1
            else:
                right = med
        if nums[left] == target:
            return left
        else:
            return -1