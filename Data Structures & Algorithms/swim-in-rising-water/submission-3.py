class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Use Dijkstra's algorithm to be greedy on the path
        # with the least time. Whatever the max time was on the path
        # that we traversed to get to the bottom right corner first,
        # is the min time to return as the answer.
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        # Keep the time in the first index of the queue so that it is
        # prioritized by time.
        q = [[grid[0][0], 0, 0]]
        # Keep track of places that have been visited.
        visit[0][0] = True
        # Easy way to traverse the different directions that are
        # available.
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Keep going until the q is empty.
        while q:
            t, i, j = heapq.heappop(q)
            # If we reached the bottom right corner, return the time.
            if i == n - 1 and j == n - 1:
                return t
            
            # Loop through the different directions.
            for di, dj in directions:
                neiI, neiJ = i + di, j + dj
                # if the coordinates are not inbounds or we already visited
                # a cell, then skip this option.
                if (neiI < 0 or neiJ < 0 or neiI >= n or
                    neiJ >= n or visit[neiI][neiJ] == True):
                    continue
                # Mark as visited
                visit[neiI][neiJ] = True
                # Store the new coordinates and the max time/height that has
                # been traversed so far on this path in the queue.
                heapq.heappush(q, [max(t, grid[neiI][neiJ]), neiI, neiJ])