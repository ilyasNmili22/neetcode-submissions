class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = (len(s) - 1) // 2
        if s[:] == s[::-1]:
            return True
        for i in range(len(s)):
            #Except i
            s_wth = s[:i] + s[i + 1:]
            print(s_wth)
            print(s_wth[-1:-n - 1:-1])
            if s_wth[:n] == s_wth[-1:-n - 1:-1]:
                return True
        return False
'''
Odd: 5
2 - 2
n // 2
Even: 6
2 - 2
(n - 1) // 2
So the med is (n - 1) // 2
'''