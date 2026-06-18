class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for u, v, w in edges:
            adj.setdefault(u, []).append((w, v))
        
        shortest = [float("inf") for node in range(n)]
        shortest[src] = 0

        q = [(0, src)]
        while q:
            curr_d, curr_node = heapq.heappop(q)

            if curr_d > shortest[curr_node]:
                continue
            
            for w, v in adj.get(curr_node, []):
                new_d = curr_d + w
                if new_d < shortest[v]:
                    shortest[v] = new_d
                    heapq.heappush(q, (new_d, v))
        
        return {i: v if v != float("inf") else -1 for i, v in enumerate(shortest)}