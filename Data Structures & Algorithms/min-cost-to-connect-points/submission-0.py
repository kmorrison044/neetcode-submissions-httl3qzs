class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhat(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        n = len(points)
        adj = {}
        for point in points:
            for p in points:
                if point != p:
                    adj.setdefault(tuple(point), []).append([manhat(point, p), p])
        
        q = [[0, points[0]]]
        res = 0
        visit = set()

        while q and len(visit) < n:
            weight, point = heapq.heappop(q)

            if tuple(point) in visit:
                continue
            
            res += weight
            visit.add(tuple(point))

            for w, nei in adj.get(tuple(point), []):
                if tuple(nei) not in visit:
                    heapq.heappush(q, [w, nei])
        
        return res
