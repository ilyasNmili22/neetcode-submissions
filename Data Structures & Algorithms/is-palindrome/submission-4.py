class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for x in s:
            if x.isalnum():
                new.append(x.upper())
        print(new)
        return new == list(reversed(new))