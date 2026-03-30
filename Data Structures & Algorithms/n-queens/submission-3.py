class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        # r + c define what pos diagnol you are on
        posDiag = set()
        # r - c define what neg diagnol you are on
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try a spot on every column to put a queen, then backtrack
            for c in range(n):
                # if the current column has already been used previously
                # or if the current positive or negative diagnol has been
                # used previously, skip placing the queen here.
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res