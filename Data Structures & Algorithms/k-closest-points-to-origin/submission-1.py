class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDistance(point):
            x1, y1 = point
            x2 = y2 = 0
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
        ret = []
        q = []
        dist_map = {}
        for point in points:
            dist = findDistance(point)
            dist_map.setdefault(dist, []).append(point)
            q.append(dist)
        heapq.heapify(q)

        while len(ret) < k:
            dist = heapq.heappop(q)
            i = 0
            while len(ret) < k and i < len(dist_map[dist]):
                ret.append(dist_map[dist][i])
                i+=1
        
        return ret

