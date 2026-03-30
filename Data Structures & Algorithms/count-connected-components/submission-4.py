class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {node: [] for node in range(n)}
        visited = set()
        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            # Simply visit the node, run through the neighbors
            # and if a neighbor has not been visited yet, run dfs
            # on that neighbor
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        # Loop through all nodes and check if the node has been visited.
        # if not, run dfs on that node and increment that count of islands.
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1 
        
        return count