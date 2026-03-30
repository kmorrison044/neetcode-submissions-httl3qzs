class Solution {
    private int maxArea = 0;
    private int ROWS, COLS;

    public int maxAreaOfIsland(int[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;

        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                maxArea = Math.max(maxArea, dfs(r, c, grid));
            }
        }

        return maxArea;
    }

    private int dfs(int r, int c, int[][] grid)
    {
        if (grid[r][c] == 0)
        {
            return 0;
        }

        int res = 1;

        grid[r][c] = 0;
        if (r + 1 < ROWS) res += dfs(r + 1, c, grid);
        if (r - 1 >= 0) res += dfs(r - 1, c, grid);
        if (c + 1 < COLS) res += dfs(r, c + 1, grid);
        if (c - 1 >= 0) res += dfs(r, c - 1, grid);

        return res;
    }
}
