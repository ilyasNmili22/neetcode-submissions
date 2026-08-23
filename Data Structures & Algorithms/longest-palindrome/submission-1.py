class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = b = 0
        for x in c.values():
            ans += (x // 2) * 2
            if x % 2:
                b = 1
        return ans + b