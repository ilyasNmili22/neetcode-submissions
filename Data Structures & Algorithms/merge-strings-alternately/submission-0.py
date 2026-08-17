class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ''
        x = 0
        for i in range(min(len(word1), len(word2))):
            ret += word1[i] + word2[i]
            x = i
        if len(word1) > len(word2):
            ret += word1[x + 1:]
        else:
            ret += word2[x + 1:]
        return ret