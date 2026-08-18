class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s, start, end,  b):
            if end - start  < 1:
                return True
            if s[start] == s[end]:
                return check(s, start + 1, end - 1, b)
            elif b == 1:
                return False
            return check(s, start + 1, end, b + 1) or check(s, start, end - 1, b + 1)
        return check(s, 0, len(s) - 1, 0)
