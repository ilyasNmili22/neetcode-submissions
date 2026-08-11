class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = sorted(intervals, key = lambda x : x[1])
        curr_end = -float('inf')
        overlap = 0
        for st, fin in arr:
            if st < curr_end:
                overlap += 1
            else:
                curr_end = fin
        return overlap