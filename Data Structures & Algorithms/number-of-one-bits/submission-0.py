class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while(n > 0):
            if (n % 2 == 1):
                s += 1
            n //= 2
        return (s)
        