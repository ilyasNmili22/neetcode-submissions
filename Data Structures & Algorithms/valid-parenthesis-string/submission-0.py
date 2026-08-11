class Solution:
    def checkValidString(self, s: str) -> bool:
        c = 0
        stack = []
        for x in s:
            if x == '*':
                c += 1
            elif x == '(':
                stack.append([x, c])
            elif x == ')' and stack:
                stack.pop()
            elif x == ')' and c:
                c -= 1
            else:
                return False
        if len(stack) > c:
            return False
        #ch7al apres
        for x in stack:
            x[1] = c - x[1]
        s = 0
        while (stack):
            if stack[-1][1] > s:
                stack.pop()
                s += 1
            else:
                return False
        return not stack