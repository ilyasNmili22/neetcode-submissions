class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s, b):
            if len(s) < 2:
                return True
            if s[-1] == s[0]:
                return check(s[1:-1], b)
            elif b == 1:
                return False
            return check(s[1:], b + 1) or check(s[:-1], b + 1)
        return check(s, 0)
