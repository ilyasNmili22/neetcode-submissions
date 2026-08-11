#Bad solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subsets = []
        def dfs(i):
            if i == len(nums):
                res.add(tuple((subsets[:])))
                return
            dfs(i + 1)
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
        nums.sort()
        dfs(0)
        return [list(x) for x in res]