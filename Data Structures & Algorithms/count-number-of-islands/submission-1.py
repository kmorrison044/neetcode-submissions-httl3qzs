class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Similar problem to backtracking, but without the backtrack

        # Initialize vars
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        # Run dfs around grid
        def dfs(r, c):
            # If this spot is water or visited, return
            if (grid[r][c] == '0'):
                return
            
            # Mark spot as visited (i.e water)
            grid[r][c] = '0'

            # Run dfs on the rest of the directions
            if r + 1 < ROWS: dfs(r + 1, c)
            if r - 1 >= 0: dfs(r - 1, c)
            if c + 1 < COLS: dfs(r, c + 1)
            if c - 1 >= 0: dfs(r, c - 1)
        
        # Iterate through grid in the parent and when you find a '1' (i.e. land),
        # run dfs and increment the island count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands