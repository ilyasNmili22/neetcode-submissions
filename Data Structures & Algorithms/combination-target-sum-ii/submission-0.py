class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ret, curr = [], []
        nums.sort()
        def dfs(start, summ):
            if summ == target:
                ret.append(curr[:])
                return
            if summ > target or start >= len(nums):
                return
            curr.append(nums[start])
            dfs(start + 1, summ + nums[start])
            curr.pop()
            while(start < len(nums) - 1 and nums[start] == nums[start + 1]):
                start += 1
            dfs(start + 1, summ)
        #print(nums) #[1, 1, 2, 5, 6, 7, 10]
        dfs(0, 0)
        return ret