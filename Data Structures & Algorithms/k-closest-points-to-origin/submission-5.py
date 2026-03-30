class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDistance(point):
            x1, y1 = point[0], point[1]
            x2 = y2 = 0
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
        ret = []
        q = []
        for point in points:
            dist = findDistance(point)
            if len(q) < k:
                heapq.heappush(q, (-dist, point))
            else:
                key = heapq.heappushpop(q, (-dist, point))
        
        return [point for _, point in q]