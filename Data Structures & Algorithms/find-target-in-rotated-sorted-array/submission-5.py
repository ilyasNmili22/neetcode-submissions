class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target <= nums[-1] or nums[-1] <= nums[m] <= target or target <= nums[-1] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
            print(l, r, m)
        return -1