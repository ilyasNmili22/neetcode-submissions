class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indx = 26 * [-1]
        for i in range(len(s)):
            indx[ord(s[i]) - ord('a')] = i
        ans = -1
        print(indx)
        for i in range(len(s)):
            alph = ord(s[i]) - ord('a')
            if indx[alph] != -1 :
                ans = max(ans, indx[alph] - i - 1)
        return ans

"""
aaaaaaaa

abca 
3 1 2 0 0...0
0

"""