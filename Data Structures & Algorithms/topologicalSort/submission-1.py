class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
        
        visited = set()
        path = set()
        ret = []

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            visited.add(node)
            path.add(node)

            for nei in adj.get(node, []):
                if not dfs(nei):
                    return False
            
            ret.append(node)
            path.remove(node)
            return True

        for node in adj:
            if not dfs(node):
                return []
        
        ret.reverse()
        return ret