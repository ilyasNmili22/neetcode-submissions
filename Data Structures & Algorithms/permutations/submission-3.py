class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []
        def dfs():
            if len(curr) == len(nums):
                ret.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    dfs()
                    curr.pop()
        dfs()
        return ret


'''
[1]                     [2]                  [3]
[1, 2]    [1, 3]      [2,1]  [2,3]        [3,1]  [3,2]
[1,2,3]   [1,3,2] ...
'''         
