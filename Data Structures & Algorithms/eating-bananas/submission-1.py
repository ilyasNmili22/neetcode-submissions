class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def CanEatAll(piles, k, h):
            s = 0
            for pile in piles:
                s += (pile + k - 1) // k
            return s <= h
        left, right = 1, max(piles)
        while(left < right):
            med = (left + right) // 2
            if CanEatAll(piles, med, h):
                right = med
            else:
                left = med + 1
        return left