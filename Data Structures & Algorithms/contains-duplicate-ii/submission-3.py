class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i, num in enumerate(nums):
            if num in my_dict and i - my_dict[num] <= k :
                return True
            else:
                my_dict[num] = i  # new one to be close to the i in the future
        return False