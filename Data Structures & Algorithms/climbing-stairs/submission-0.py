class Solution:
    def climbStairs(self, n: int) -> int:
        ret = [0, 1]
        for i in range(n):
            ret.append(ret[-1] + ret[-2])
        return ret[-1]
