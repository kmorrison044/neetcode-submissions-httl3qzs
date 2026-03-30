class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # This dfs will simply check if the element is "O", and if it is, 
        # We will mark it as "S" (safe) and continue with the dfs, otherwise,
        # return out of the function call.
        def dfs(r, c):
            if board[r][c] != "O":
                return

            board[r][c] = "S"
            if r + 1 < ROWS: dfs(r + 1, c)
            if r - 1 >= 0: dfs(r - 1, c)
            if c + 1 < COLS: dfs(r, c + 1)
            if c - 1 >= 0: dfs(r, c - 1)

        # We know that all elements on the edges of the board are safe.
        # Begin with these elements and mark them as safe and then run dfs
        # and grab any adjacent elements that are also "O"s and mark them as
        # safe as well.
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

        # Now iterate through all cells, and if they are marked "O", we know they
        # are surronded and can be marked as "X". Then we can see if it is marked as
        # "S" and if so, change it back to "O".
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"