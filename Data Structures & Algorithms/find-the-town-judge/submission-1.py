class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        trusted = {}
        ans = 0
        for x in trust:
            trusted[x[0]] = -1
            if x[1] not in trusted or trusted[x[1]] != -1:
                trusted[x[1]] =  trusted.get(x[1], 0) + 1
        for x in trusted:
            if trusted[x] == n - 1:
                return x
        return -1
