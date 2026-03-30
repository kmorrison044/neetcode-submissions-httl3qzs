class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Define distance function to calculate distance
        def findDistance(point):
            x1, y1 = point[0], point[1]
            x2 = y2 = 0
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
        ret = []
        q = []
        # Iterate through the points and calculate distance
        for point in points:
            dist = findDistance(point)
            # if the length of the q is less than k, then push to the heap
            # with the distance as the first part of the tuple (the first part
            # of the tuple is what is compared on the heap)
            if len(q) < k:
                heapq.heappush(q, (-dist, point))
            # Otherwise do a heappushpop, which is more efficient than heappush then a heappop
            else:
                key = heapq.heappushpop(q, (-dist, point))
        
        # Return the second part of the tuple (the point) for everything in the q
        return [point for _, point in q]