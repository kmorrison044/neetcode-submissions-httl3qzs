class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Set constants and return vals
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # If it is water or has been visited, return
            if grid[r][c] == 0:
                return 0

            # Mark land as visited (i.e. water)
            grid[r][c] = 0
            # Set return var in dfs. This is necessary to collect the area in all
            # directions.
            res = 0
            if r + 1 < ROWS: res += dfs(r + 1, c)
            if r - 1 >= 0: res += dfs(r - 1, c)
            if c + 1 < COLS: res += dfs(r, c + 1)
            if c - 1 >= 0: res += dfs(r, c - 1)

            # Return the result plus 1 to include this piece of land in the area
            return res + 1

        # Iterate over the grid starting at every cell and run dfs when you reach land.
        # update max area with the return of dfs for a single island.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area