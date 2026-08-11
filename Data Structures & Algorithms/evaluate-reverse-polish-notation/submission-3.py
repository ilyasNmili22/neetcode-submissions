class Solution:
    def fct(self,n1,n2,c):
        if c=="+":
            return n1+n2
        elif c=="-":
            return n1-n2
        elif c=="*":
            return n1*n2
        elif n2!=0:
            return int(n1/n2)
        return 0
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for car in tokens:
            if car in "+-*/":
                s = Solution().fct(stack[-2],stack[-1],car)
                stack.pop()
                stack.pop()
                
                stack.append(s)

            else:
                stack.append(int(car))
            print(stack)
        return stack[-1]