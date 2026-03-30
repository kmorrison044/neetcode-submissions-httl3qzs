class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, area):
            nonlocal max_area

            if grid[r][c] == 0:
                return

            area[0] += 1
            max_area = max(max_area, area[0])
            grid[r][c] = 0
            if r + 1 < ROWS: dfs(r + 1, c, area)
            if r - 1 >= 0: dfs(r - 1, c, area)
            if c + 1 < COLS: dfs(r, c + 1, area)
            if c - 1 >= 0: dfs(r, c - 1, area)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c, [0])
        
        return max_area