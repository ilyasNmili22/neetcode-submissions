class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {} # index : val
        for i in range(len(nums)):
            diff = target - nums[i] # le besoin pour obtenir une somme de target
            if diff in Map:
                return [Map[diff], i]
            Map[nums[i]] = i
        