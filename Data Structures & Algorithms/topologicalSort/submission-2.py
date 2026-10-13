class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for u, v in edges:
            adj.setdefault(u, []).append(v)
        
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

        for i in range(n):
            if not dfs(i):
                return []
        
        ret.reverse()
        return ret