class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while(n):
            n &= n - 1
            s += 1
        return s
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1):
            arr.append(self.hammingWeight(i))
        return arr