class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []
        def dfs(i):
            if i == len(nums):
                ret.append(curr[:])
                return
            dfs(i + 1)
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
        dfs(0)
        return ret
