class Solution:
    def checkValidString(self, s: str) -> bool:
        et = []
        par = []
        for i, x in enumerate(s):
            if x == '*':
                et.append(i)
            elif x == '(':
                par.append(i)
            elif x == ')' and par:
                par.pop()
            elif x == ')' and et:
                et.pop()
            else:
                return False
        if len(par) > len(et):
            return False
        #ch7al apres, prob (* and *)
        while(par):
            if par[-1] < et[-1]:
                par.pop()
                et.pop()
            else:
                return False
        return True