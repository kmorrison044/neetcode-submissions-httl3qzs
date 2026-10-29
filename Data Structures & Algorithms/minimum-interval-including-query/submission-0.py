class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        priQ = []
        intervals.sort(key=lambda x : (x[0], x[1]))
        res = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(priQ, (r - l + 1, r))
                i += 1
            
            while priQ and priQ[0][1] < q:
                heapq.heappop(priQ)
            res[q] = priQ[0][0] if priQ else -1
        
        return [res[q] for q in queries]