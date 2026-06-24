class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhat(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        n = len(points)
        adj = {}
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhat(points[i], points[j])
                adj.setdefault(i, []).append([dist, j])
                adj.setdefault(j, []).append([dist, i])
        
        q = [[0, 0]]
        res = 0
        visit = set()

        while q and len(visit) < n:
            weight, point = heapq.heappop(q)

            if point in visit:
                continue
            
            res += weight
            visit.add(point)

            for w, nei in adj.get(point, []):
                if nei not in visit:
                    heapq.heappush(q, [w, nei])
        
        return res