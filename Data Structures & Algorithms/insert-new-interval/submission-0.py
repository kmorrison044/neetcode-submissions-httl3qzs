class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        l, r = 0, len(intervals) - 1
        target = newInterval[0]

        while l <= r:
            mid = l + (r - l // 2)
            if intervals[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        intervals.insert(l, newInterval)

        res = []
        for it in intervals:
            if not res or res[-1][1] < it[0]:
                res.append(it)
            else:
                res[-1][1] = max(res[-1][1], it[1])
        
        return res