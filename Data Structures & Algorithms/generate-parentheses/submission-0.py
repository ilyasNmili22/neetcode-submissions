class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [set() for j in range(n + 1)]
        dp[0].add("")
        for i in range(1, n + 1):
            for string in dp[i - 1]:
                for j in range(len(string)):
                    if string[j] == ')':
                        dp[i].add(string[:j] + '(' + '))' + string[j + 1:])
                dp[i].add(string + '()')
        return list(dp[-1])