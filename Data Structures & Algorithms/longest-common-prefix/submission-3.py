class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        rep = ''
        for i in range (l):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return rep
            rep += strs[0][i]
        return rep

