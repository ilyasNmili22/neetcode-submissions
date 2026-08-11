class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sorted_c = sorted(c.items(), key = lambda x : -x[1])
        return [x[0] for x in sorted_c[:k]]