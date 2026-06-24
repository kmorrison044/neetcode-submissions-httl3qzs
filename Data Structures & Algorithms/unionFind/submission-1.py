class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_y, root_x = root_x, root_y
        else:
            self.size[root_x] += 1
        self.parent[root_y] = root_x
        # self.size[root_x] += self.size[root_y]
        self.n -= 1
        return True

    def getNumComponents(self) -> int:
        return self.n