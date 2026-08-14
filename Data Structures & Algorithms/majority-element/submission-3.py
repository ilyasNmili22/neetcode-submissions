class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for x in nums:
            if x in my_dict:
                my_dict[x] += 1
            else:
                my_dict[x] = 1
            # generalize for size = 1
            if my_dict[x] > len(nums) // 2:
                    return x
        return -1