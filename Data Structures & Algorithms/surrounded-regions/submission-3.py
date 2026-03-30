class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if board[r][c] != "O":
                return

            board[r][c] = "S"
            if r + 1 < ROWS: dfs(r + 1, c)
            if r - 1 >= 0: dfs(r - 1, c)
            if c + 1 < COLS: dfs(r, c + 1)
            if c - 1 >= 0: dfs(r, c - 1)

        for r in range(ROWS):
            if board[r][COLS-1] == "O":
                dfs(r, COLS-1)

            if board[r][0] == "O":
                dfs(r, 0)

        for c in range(COLS):
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)

            if board[0][c] == "O":
                dfs(0, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"