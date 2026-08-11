class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = sorted(intervals, key = lambda x : x[1])
        curr_end = -float('inf')
        ret = 0
        for st, fin in arr:
            if st >= curr_end:
                print(st, curr_end)
                ret += 1
                curr_end = fin
        return len(intervals) - ret