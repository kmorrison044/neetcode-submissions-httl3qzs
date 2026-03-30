class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {node: [] for node in range(n)}
        visited = set()
        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            count += 1 
        
        return count