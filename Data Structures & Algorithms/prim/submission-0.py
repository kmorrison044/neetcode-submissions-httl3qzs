class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for u, v, w in edges:
            adj.setdefault(u, []).append([w, v])
            adj.setdefault(v, []).append([w, u])
        
        q = [[0, 0]]
        res = 0
        visit = set()
        while q and len(visit) < n:
            weight, node = heapq.heappop(q)
            if node in visit:
                continue
            
            res += weight
            visit.add(node)

            for w, nei in adj.get(node, []):
                if nei not in visit:
                    heapq.heappush(q, [w, nei])
        
        return res if len(visit) == n else -1