class Solution:
    def maxScore(self, s: str) -> int:
        zero, one = 0, s.count('1')
        ans = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            ans = max(ans, zero + one)
        return ans




'''
1 1 1 1 2 2
4 4 3 2 1 1   -> 1 1 2 3 4 4
max(zeros[i] + ones[i + 1])

'''