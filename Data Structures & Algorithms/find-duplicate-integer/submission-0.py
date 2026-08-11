class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict = {}
        for e in nums:
            if e in my_dict:
                my_dict[e] += 1
            else:
                my_dict[e] = 1
        for key, value in my_dict.items():
            if value > 1:
                return key
        return 0