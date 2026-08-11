class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        n = len(nums)
        i = 0
        for i in range(n):
            if nums[i] > 0:break
            if i > 0 and nums[i] == nums[i - 1]:continue
            l = i + 1
            r = n - 1
            while (l < r):
                if nums[r] < 0:break
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
                while (i + 1 < l < r and nums[l] == nums[l - 1]):
                    l += 1
                while (l < r < n - 1 and nums[r] == nums[r + 1]):
                    r -= 1
        return ret