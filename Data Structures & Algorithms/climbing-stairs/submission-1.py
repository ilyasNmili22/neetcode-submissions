class Solution:
    def climbStairs(self, n: int) -> int:
        v1, v2 = 0, 1
        for i in range(n):
            v1 = v1 + v2
            v1, v2 = v2, v1
        return v2