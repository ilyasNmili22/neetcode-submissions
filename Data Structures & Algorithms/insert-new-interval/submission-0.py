class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start > newInterval[1]:
                return ret + [newInterval] + intervals[i:]
            elif end < newInterval[0]:
                ret.append(intervals[i])
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        return ret + [newInterval]