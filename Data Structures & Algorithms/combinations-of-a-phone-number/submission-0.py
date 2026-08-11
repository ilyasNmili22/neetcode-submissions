class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        ret, curr = [], []
        if not digits: return ret
        def dfs(i):
            if i == len(digits):
                ret.append("".join(curr[:]))
                return
            for x in my_dict[digits[i]]:
                curr.append(x)
                dfs(i + 1)
                curr.pop()
        dfs(0)
        return ret
                    