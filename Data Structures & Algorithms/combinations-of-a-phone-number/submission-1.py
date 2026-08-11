class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        ret = []
        def dfs(i, curr):
            if i == len(digits):
                ret.append(curr)
                return
            for x in my_dict[digits[i]]:
                dfs(i + 1, curr + x)
        if digits:
            dfs(0, '')
        return ret
                    