class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Do Backtrack with for loop determining the starting point
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r: int, c: int, i: int):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False
            
            # Choose the current element
            board[r][c] = '#'
            res = (backtrack(r - 1, c, i + 1) or
                   backtrack(r + 1, c, i + 1) or
                   backtrack(r, c - 1, i + 1) or
                   backtrack(r, c + 1, i + 1))

            # Don't choose the current element. This works because the if
            # statement above checks if word[i] == the current element.
            # if it did not, then it wouldn't get here:
            board[r][c] = word[i]

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False