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
            dist_map.setdefault(-dist, []).append(point)
            heapq.heappush(q, -dist)
            if len(q) > k:
                key = heapq.heappop(q)
                dist_map[key].pop()
                if not dist_map[key]:
                    del dist_map[key]
                    print(dist_map)

        # while q:
        #     ret.append(dist_map[heapq.heappop(q)].pop())
        
        return [pt for pts in dist_map.values() for pt in pts]