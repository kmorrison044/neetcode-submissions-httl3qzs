class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            res = 0
            if r + 1 < ROWS: res += dfs(r + 1, c)
            if r - 1 >= 0: res += dfs(r - 1, c)
            if c + 1 < COLS: res += dfs(r, c + 1)
            if c - 1 >= 0: res += dfs(r, c - 1)

            return res + 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area