class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while (l < r):
            m = (l + r) // 2
            s = 0
            #check if m is valid
            for x in piles:
                s += (x + m - 1) // m
                if s > h:
                    break
            #m is not valid
            if s > h :
                l = m + 1
            else:
                r = m
        return r

