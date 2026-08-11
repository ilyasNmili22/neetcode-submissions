class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = {n}
        while(n != 1):
            n = sum([int(x) ** 2 for x in str(n)])
            if n in my_set:
                return False
            my_set.add(n)
        return True