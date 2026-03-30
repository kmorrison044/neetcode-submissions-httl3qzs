class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {node: [] for node in range(n)}
        visited = set()

        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)

        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n