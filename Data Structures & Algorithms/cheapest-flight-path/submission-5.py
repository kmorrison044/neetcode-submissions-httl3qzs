class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = []
        adj = {}
        for frm, to, price in flights:
            adj.setdefault(frm, []).append([to, price])
        
        q.append([0, src, 0])
        # Normal dijkstra would keep a set of visited nodes so that we don't visit
        # the same node infinite number of times, but in this case, we have a
        # "max_stops" constraint, so while it could be cheaper to get to a particular
        # point, we may run out of stops before we get to a destination. Therefore,
        # we keep a "best_stops" map that maps a node to the cheapest number of stops
        # it took to get to a node at a particular time.
        best_stops = {}
        while q:
            cost, node, stops = heapq.heappop(q)
            if node == dst:
                return cost
            # If we reached the limit, or we got to the node at a fewer number
            # of stops / cost, then we skip processing.
            if stops > k or stops >= best_stops.get(node, float('inf')):
                continue
            
            best_stops[node] = stops
            for nei, price in adj.get(node, []):
                heapq.heappush(q, [price + cost, nei, stops + 1])
        
        # Return -1 if there was no possible path to get to the destination
        # in the required number of stops.
        return -1