#print(math.log2(1000)) = pres 10 < 16 = 32 // 2
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b != 0):
            x1 = a ^ b
            x2 = (a & b) << 1
            a = x1 & mask
            b = x2 & mask
        print(bin(a))
        if a >= 2**31:
            return -(2**32 - a)
        return a