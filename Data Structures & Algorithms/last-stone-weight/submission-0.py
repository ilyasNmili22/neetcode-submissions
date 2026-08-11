from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)
        while (len(stones) > 1):
            a = heappop(stones) # -8
            b = heappop(stones) # -7
            if a != b:
                heappush(stones, a - b)
        
        return -stones[0] if stones else 0 