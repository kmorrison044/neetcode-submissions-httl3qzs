class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Create the board full of "."
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r: int) -> None:
            # if you get to the end of the board, copy the board to the 
            # output format and append to res
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # Your choice is to put the Q on this column or not. Iterate
            # through every column, check to see if it would be a valid placement,
            # if so, try putting the queen there and do the recursive call to
            # backtrack. Then reset it back to "." and try the next col.
            for c in range(n):
                if self.isValid(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
        backtrack(0)
        return res

    # Main func to check if board would be valid if a queen was placed
    # at r, c.
    def isValid(self, r, c, board):
        # Check vertical attack position
        row, col = r, c
        while row >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
        
        # Check left diagnol
        row, col = r, c
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Check right diagnol
        row, col = r, c
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        
        return True
