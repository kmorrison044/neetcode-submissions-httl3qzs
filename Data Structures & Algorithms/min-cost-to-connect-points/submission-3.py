class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0] * n
        self.n = n
    
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
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        
        return True

class Solution:
    def manhattan(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        q = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = self.manhattan(points[i], points[j])
                heapq.heappush(q, [dist, i, j])

        uf = UnionFind(n)
        numEdges = 0
        res = 0
        while q and numEdges < n - 1:
            d, u, v = heapq.heappop(q)
            if uf.union(u, v):
                res += d

        return res