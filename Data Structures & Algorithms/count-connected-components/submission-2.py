class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {node: [] for node in range(n)}
        visited = set()
        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, par):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node)
        
        for node in range(n):
            if node in visited:
                continue
            dfs(node, -1)
            count += 1 
        
        return count