class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = [[0] * 26 for i in range(len(words))]
        for i in range(len(words)):
            for x in words[i]:
                arr[i][ord(x) - ord('a')] += 1
        ans = []
        for i in range(26):
            mn = 100
            for j in range(len(words)):
                mn = min(mn, arr[j][i])
            ans += mn * [chr(ord('a') + i)]
        return ans
