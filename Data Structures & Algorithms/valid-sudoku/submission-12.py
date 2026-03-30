class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_idx = 0
        col_idx = 0
        count = 0
        for i in range(9):
            targ = [col for col in board[i] if col != "."]
            set_n = set(targ)
            count += len(targ) == len(set_n)

            targ = [row[i] for row in board if row[i] != "."]
            set_n = set(targ)
            count += len(targ) == len(set_n)

            if i % 3 == 0 and i > 0:
                row_idx += 3
                col_idx = 0
            targ = []
            for x in range(3):
                targ.extend([item for item in board[row_idx+x][col_idx:col_idx+3] if item != "."])
            col_idx += 3

            set_n = set(targ)
            count += len(targ) == len(set_n)
            
        return count == 27
