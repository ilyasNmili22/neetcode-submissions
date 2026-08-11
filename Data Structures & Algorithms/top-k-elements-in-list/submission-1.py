class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        min_heap = []
        for key, v in c.items():
            heapq.heappush(min_heap, (v, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [x[1] for x in min_heap]

        