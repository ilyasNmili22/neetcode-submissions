class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ret = last = first = 0
        while (last < n - 1):
            next_last = 0
            for i in range(first, last + 1):
                next_last = max(next_last, i + nums[i])
            ret += 1
            first = last + 1
            last = next_last
        
        return ret
