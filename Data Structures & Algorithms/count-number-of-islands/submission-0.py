class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (grid[r][c] == '0'):
                return
            
            grid[r][c] = '0'
            if r + 1 < ROWS: dfs(r + 1, c)
            if r - 1 >= 0: dfs(r - 1, c)
            if c + 1 < COLS: dfs(r, c + 1)
            if c - 1 >= 0: dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands