class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_sum = 1
        for i in range(len(s) - 1):
            j = i + 1
            my_set = set(s[i])
            while (j < len(s) and s[j] not in my_set):
                my_set.add(s[j])
                j += 1
            max_sum = max(max_sum, j - i)    
        return max_sum