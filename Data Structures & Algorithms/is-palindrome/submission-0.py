class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [c for c in s if c.isalnum()]
        res = ("".join(res)).lower()
        return res == res[::-1]