class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                for w in wordDict:
                    if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                        dp[i + len(w) - 1] = 1
        return dp[-1] == 1