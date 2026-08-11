class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for num in my_set:
            if num - 1 not in my_set: #O(1)
                curr = 1
                while(num + curr in my_set):
                    curr += 1
                longest = max(longest, curr)
        return longest