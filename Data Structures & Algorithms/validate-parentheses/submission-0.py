class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for c in s:
            if c not in my_dict:
                stack.append(c)
            elif not stack or stack[-1] != my_dict[c]:
                return False
            else:
                stack.pop()
        return not stack #len(stack) == 0

