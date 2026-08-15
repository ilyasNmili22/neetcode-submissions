class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while (l <= r):
            m = (l + r) // 2
            if m * m == x:
                return m
            if m * m > x:
                r = m - 1
            else:
                l = m + 1
        
        return r


"""
x = 13
l = 0, r = 13
m = 6
m * m = 36 > x
r = 5

l = 0, r = 5
m = 2 
m * m = 4 < x
l = 2, r = 5


"""