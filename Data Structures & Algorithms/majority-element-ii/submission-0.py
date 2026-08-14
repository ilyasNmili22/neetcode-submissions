class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = {}
        for x in nums:
            my_dict[x] = my_dict.get(x, 0) + 1
        ret = []
        for x in my_dict:
            if my_dict[x] > len(nums) // 3:
                ret += [x]
        return ret