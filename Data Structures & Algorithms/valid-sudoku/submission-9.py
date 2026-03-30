class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        col = []
        sq = []
        row_idx = 0
        col_idx = 0
        for i in range(9):
            targ_r = [col for col in board[i] if col != "."]
            nums_set_r = set(targ_r)
            row.append(len(targ_r) == len(nums_set_r))

            targ_c = [row[i] for row in board if row[i] != "."]
            nums_set_c = set(targ_c)
            col.append(len(targ_c) == len(nums_set_c))

            if i % 3 == 0 and i > 0:
                row_idx += 3
                col_idx = 0
            targ_sq = []
            for x in range(3):
                targ_sq.extend([item for item in board[row_idx+x][col_idx:col_idx+3] if item != "."])
            col_idx += 3

            nums_set_sq = set(targ_sq)
            sq.append(len(targ_sq) == len(nums_set_sq))
            
            

        print(sum(sq))
        print(sum(row))
        print(sum(col))
        return sum(row) == sum(col) == sum(sq) == 9
