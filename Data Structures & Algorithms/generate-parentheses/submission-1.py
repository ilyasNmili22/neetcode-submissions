class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(string):
            if len(string) == 2 * n:
                res.append(string)
            if string.count('(') < n:
                backtrack(string + '(')
            if string.count('(') > string.count(')'):
                backtrack(string + ')')
        backtrack("")
        return res