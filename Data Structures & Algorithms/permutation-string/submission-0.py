class Solution:
    def is_anagram(self, s1, s2):
        alph1 = 26 * [0]
        alph2 = 26 * [0]
        for c in s1:
            alph1[ord(c) - ord('a')] += 1
        for c in s2:
            alph2[ord(c) - ord('a')] += 1
        for i in range(26):
            if alph1[i] != alph2[i]:
                return 0
        return 1
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1) #2
        if len(s1) > len(s2):
            return False
        for i in range(len(s2) - n + 1): #8 - 2
            if self.is_anagram(s1, s2[i: i + n]):
                return True
        return False