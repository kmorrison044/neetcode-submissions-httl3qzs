class Solution {
    public int orangesRotting(int[][] grid) {
        final int ROWS = grid.length;
        final int COLS = grid[0].length;
        final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int fresh = 0;
        int time = 0;
        Queue<int[]> q = new ArrayDeque<>();

        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                if (grid[r][c] == 1)
                {
                    fresh += 1;
                }
                if (grid[r][c] == 2)
                {
                    q.offer(new int[] {r, c});
                }
            }
        }

        while (fresh > 0 && !q.isEmpty())
        {
            int length = q.size();
            for (int i = 0; i < length; i++)
            {
                int[] node = q.poll();
                int r = node[0];
                int c = node[1];

                for (int[] dir : DIRS)
                {
                    int row = r + dir[0];
                    int col = c + dir[1];

                    if (row < ROWS && col < COLS && row >= 0 && col >= 0 &&
                        grid[row][col] == 1)
                    {
                        grid[row][col] = 2;
                        q.offer(new int[] {row, col});
                        fresh--;
                    }
                }
            }
            time++;
        }
        return fresh == 0 ? time : -1;
    }
}
