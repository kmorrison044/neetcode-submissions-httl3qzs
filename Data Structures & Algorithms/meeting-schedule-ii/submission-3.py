"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for it in intervals:
            times.append([it.start, 1])
            times.append([it.end, -1])

        times.sort(key=lambda x : (x[0], x[1]))

        count = res = 0
        for t in times:
            count += t[1]
            res = max(res, count)
        
        return res