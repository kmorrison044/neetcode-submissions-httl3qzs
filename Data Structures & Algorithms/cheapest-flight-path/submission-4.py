class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = []
        adj = {}
        for frm, to, price in flights:
            adj.setdefault(frm, []).append([to, price])
        
        q.append([0, src, 0])
        best_stops = {}
        while q:
            cost, node, stops = heapq.heappop(q)
            if node == dst:
                return cost
            if stops > k or stops >= best_stops.get(node, float('inf')):
                continue
            
            best_stops[node] = stops
            for nei, price in adj.get(node, []):
                heapq.heappush(q, [price + cost, nei, stops + 1])
        
        return -1