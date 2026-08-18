class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while (l < r):
            if s[l] != s[r]:
                rm_l = s[:l] + s[l + 1:]
                rm_r = s[:r] + s[r + 1:]
                return rm_l == rm_l[::-1] or rm_r == rm_r[::-1]
            l += 1
            r -= 1
        return True

"""
abcbja  -> abcba
> bcbj
> bcb or cbj

n + n + n + ... + n (n times) = n²
1 + 1 + ... + n eq O(n) 
"""