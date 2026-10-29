class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Storing the length of the valid interval and the right bound of the interval
        priQ = []
        # Sort intervals to work from left to right
        intervals.sort(key=lambda x : (x[0], x[1]))
        # Map the query to the result
        res = {}
        # Start at the first index of the sorted intervals
        i = 0

        # Iterate through the queries in sorted order to to naturally progress from the smallest
        # possible interval to the largest.
        for q in sorted(queries):
            # While we are in bounds and the query is greater than the leftmost point
            while i < len(intervals) and intervals[i][0] <= q:
                # Grab the left and right boundaries of the interval
                l, r = intervals[i]
                # Push potential interval to the queue by storing the length and rightmost boundary
                heapq.heappush(priQ, (r - l + 1, r))
                # Iterate through the interval
                i += 1
            
            # While the priQ is not empty and the query is outside of the interval to the right
            while priQ and priQ[0][1] < q:
                # Pop the invalid interval from the heap
                heapq.heappop(priQ)
            # Once all invalid intervals are gone, the smallest interval is stored at the front of the queue, otherwise
            # there are no valid intervals, so add -1.
            res[q] = priQ[0][0] if priQ else -1
        
        # Convert the hashmap to a list for return.
        return [res[q] for q in queries]