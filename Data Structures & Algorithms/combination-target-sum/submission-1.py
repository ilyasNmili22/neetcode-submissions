class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret, curr = [], []
        def dfs(start, summ):
            if summ == target:
                ret.append(curr[:])
                return
            if summ > target:
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i, summ + nums[i])
                curr.pop()
        dfs(0, 0)
        return ret