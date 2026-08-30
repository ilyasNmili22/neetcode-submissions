class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        for i in range(k):
            gifts[-1] = floor(sqrt(gifts[-1]))
            gifts.sort()
        return sum(gifts)