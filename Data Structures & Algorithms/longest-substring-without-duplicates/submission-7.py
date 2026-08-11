class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        my_set = set()
        max_P = 0
        for r in range(len(s)):
            while (s[r] in my_set):
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            max_P = max(max_P, len(my_set)) #r - l
        return max_P
