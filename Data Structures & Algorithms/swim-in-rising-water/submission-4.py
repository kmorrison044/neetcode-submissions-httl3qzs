class DSU:
    def __init__(self, n):
        # Make each coordinate it's parent
        self.parent = [i for i in range(n + 1)]
        # Every component intialized with size of 1
        self.size = [1] * (n + 1)
    
    def find(self, node):
        # if the node is the root of the tree, then its parent
        # is itself. So recursively call the function until this
        # condition is met to find the parent node. Setting all
        # the parents to the actual root makes future calls more
        # efficient.
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        # to join two nodes together, find the parent's of both nodes
        pu = self.find(u)
        pv = self.find(v)
        # if they have the same parent, they are already connected.
        if pu == pv:
            return False
        # Whichever parent has the greater size, incorporate the smaller
        # tree into the bigger one.
        if self.size[pu] < self.size[pv]:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        else:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        
        # We successfully united the two nodes
        return True
    
    def isConnected(self, u, v):
        # We know 2 nodes are connected if the share the same parent.
        return self.find(u) == self.find(v)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Flatten the 2d grid
        dsu = DSU(n * n)
        # Throw all points into a priority queue based on time
        q = [[grid[r][c], r, c] for r in range(n) for c in range(n)]
        heapq.heapify(q)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # while q is not empty
        while q:
            # Grab current smallest time and coordinates
            t, r, c = heapq.heappop(q)
            # Check all directions and see if there is an adjacent cell
            # that is less than or equal too the current time. If so,
            # join them together.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
                    # convert to flattened coordinates using standard formula
                    dsu.union(r * n + c, nr * n + nc)
            
            # Before going to the next iteration, if the first cell
            # and last cell are connected, then we found the solution.
            if dsu.isConnected(0, n * n - 1):
                # The current time is the minimum time it would take
                # to connect the initial and target cells.
                return t