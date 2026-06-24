class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0] * n
        self.comp = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.size[root_x] > self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += root_y
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += root_x
        
        self.comp -= 1
        return True
    
    def isSameComponent(self, x, y):
        return self.find(x) == self.find(y)
    
    def numComponents(self):
        return self.comp
    
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        q = []
        for u, v, w in edges:
            heapq.heappush(q, [w, u, v])
        
        uf = UnionFind(n)
        res = 0
        numEdges = 0
        while numEdges < n - 1 and q:
            w, u, v = heapq.heappop(q)
            if not uf.union(u, v):
                continue
            res += w
            numEdges += 1
        
        return res if numEdges == n - 1 else -1