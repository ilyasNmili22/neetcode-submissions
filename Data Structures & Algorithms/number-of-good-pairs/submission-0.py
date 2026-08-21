class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums).values()
        s = 0
        for x in c:
            s += x * (x - 1) // 2
        return s

"""
2 > 1
3 > 3
4 > 6
x -> fact(x - 1)
"""