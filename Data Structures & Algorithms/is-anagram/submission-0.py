class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        arr1 = 26 * [0]
        arr2 = 26 * [0]
        for i in range(n):
            arr1[ord(s[i]) - ord('a')] += 1
            arr2[ord(t[i]) - ord('a')] += 1
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False
        return True
        
        