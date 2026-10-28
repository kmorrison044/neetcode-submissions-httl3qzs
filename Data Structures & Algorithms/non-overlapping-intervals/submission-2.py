class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        out = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start >= prevEnd:
                prevEnd = end
            else:
                out += 1
                prevEnd = min(end, prevEnd)
        
        return out