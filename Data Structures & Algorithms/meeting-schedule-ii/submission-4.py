"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startend = [(x.start, 1) for x in intervals] + [(x.end, -1) for x in intervals]
        startend.sort(key = lambda x : (x[0], x[1]))
        mx = curr = 0
        for x, y in startend:
            curr += y
            mx = max(mx, curr)
        return mx