class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()
        for x in nums:
            if x in my_set:
                return x
            my_set.add(x)
        return 0