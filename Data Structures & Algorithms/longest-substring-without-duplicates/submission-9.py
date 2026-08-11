class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        my_dict = {}
        maxL = 0
        for r in range(len(s)):
            if s[r] in my_dict:
                l = max(my_dict[s[r]] + 1, l)                
            maxL = max(maxL, r - l + 1)
            my_dict[s[r]] = r
        return maxL
