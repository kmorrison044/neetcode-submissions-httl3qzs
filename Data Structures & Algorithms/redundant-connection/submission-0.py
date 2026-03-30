class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        cycle = set()
        cycleStart = -1
        visited = set()
        adj = {node: [] for node in range(n + 1)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, par):
            nonlocal cycleStart

            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True

            return False
        
        dfs(1, -1)
        for i in range(n-1, -1, -1):
            u, v = edges[i]
            if u in cycle and v in cycle:
                return [u, v]

