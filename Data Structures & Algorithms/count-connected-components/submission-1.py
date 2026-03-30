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
        
        i = 0
        while len(visited) < n:
            if i in visited:
                i += 1
                continue
            dfs(i, -1)
            count += 1 
            i += 1
        
        return count