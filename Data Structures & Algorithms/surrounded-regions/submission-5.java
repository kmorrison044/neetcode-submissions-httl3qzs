class Solution {
    public void solve(char[][] board) {
        final int ROWS = board.length, COLS = board[0].length;

        for (int r = 0; r < ROWS; r++)
        {
            if (board[r][COLS - 1] == 'O')
            {
                dfs(r, COLS-1, board);
            }
            if (board[r][0] == 'O')
            {
                dfs(r, 0, board);
            }
        }

        for (int c = 0; c < COLS; c++)
        {
            if (board[ROWS-1][c] == 'O')
            {
                dfs(ROWS-1, c, board);
            }
            if (board[0][c] == 'O')
            {
                dfs(0, c, board);
            }
        }

        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                if (board[r][c] == 'O')
                {
                    board[r][c] = 'X';
                }
                if (board[r][c] == 'S')
                {
                    board[r][c] = 'O';
                }
            }
        }
    }

    public void dfs(int r, int c, char[][] board)
    {
        final int ROWS = board.length, COLS = board[0].length;

        if (board[r][c] != 'O')
        {
            return;
        }

        board[r][c] = 'S';
        if (r + 1 < ROWS) dfs(r + 1, c, board);
        if (r - 1 >= 0) dfs(r - 1, c, board);
        if (c + 1 < COLS) dfs(r, c + 1, board);
        if (c - 1 >= 0) dfs(r, c - 1, board);
    }
}
