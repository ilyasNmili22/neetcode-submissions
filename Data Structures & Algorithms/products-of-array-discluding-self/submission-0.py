def product(arr, n):
    p = 1
    for i in range(len(arr)):
        if i != n:
            p *= arr[i]
    return p

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(product(nums, i))
        return ret 