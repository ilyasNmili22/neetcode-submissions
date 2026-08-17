class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        my_dict = {}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = [i, i]
            else:
                my_dict[s[i]][0] = min(i, my_dict[s[i]][0])
                my_dict[s[i]][1] = max(i, my_dict[s[i]][1])
        ans = -1
        for a, b in my_dict.values():
            ans = max(ans, b - a - 1)
        return ans