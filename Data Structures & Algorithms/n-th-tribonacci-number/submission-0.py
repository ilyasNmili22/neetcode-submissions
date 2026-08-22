class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            tmp = a + b + c
            a = b
            b = c
            c = tmp
        return c
            
