class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for u, v in edges:
            adj.setdefault(u, []).append(v)
        
        visited = {}
        ret = []

        def dfs(node):
            if node in visited:
                return not visited[node]
            
            visited[node] = True

            for nei in adj.get(node, []):
                if not dfs(nei):
                    return False
            
            ret.append(node)
            visited[node] = False
            return True

        for i in range(n):
            if not dfs(i):
                return []
        
        ret.reverse()
        return ret