class Solution:
    def maxScore(self, s: str) -> int:
        zeros = [1 if s[0] == '0' else 0]
        for x in s[1:]:
            if x == '0':
                zeros.append(zeros[-1] + 1)
            else:
                zeros.append(zeros[-1])
        ones = [1 if s[-1] == '1' else 0]

        for x in s[::-1][1:]:
            if x == '1':
                ones.append(ones[-1] + 1)
            else:
                ones.append(ones[-1])
        ones.reverse()
        ans = 0
        for i in range(len(s) - 1):
            ans = max(ans, zeros[i] + ones[i + 1])
        #print(zeros, ones)
        return ans
'''
1 1 1 1 2 2
4 4 3 2 1 1   -> 1 1 2 3 4 4
max(zeros[i] + ones[i + 1])

'''