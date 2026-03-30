class Solution {
    private int islands = 0;

    public int numIslands(char[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;

        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                if (grid[r][c] == '1')
                {
                    dfs(r, c, grid);
                    islands++;
                }
            }
        }

        return islands;
    }

    private void dfs(int r, int c, char[][] grid)
    {
        int ROWS = grid.length, COLS = grid[0].length;

        if (grid[r][c] == '0')
        {
            return;
        }

        grid[r][c] = '0';
        if (r + 1 < ROWS) dfs(r + 1, c, grid);
        if (r - 1 >= 0) dfs(r - 1, c, grid);
        if (c + 1 < COLS) dfs(r, c + 1, grid);
        if (c - 1 >= 0) dfs(r, c - 1, grid);
    }
}
