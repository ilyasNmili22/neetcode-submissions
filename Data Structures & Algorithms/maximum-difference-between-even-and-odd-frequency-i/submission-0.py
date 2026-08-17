class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        odd = [x for x in c.values() if x % 2]
        even = [x for x in c.values() if x % 2 == 0]
        
        return max(odd) - min(even)