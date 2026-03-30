class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        col = []
        sq = []
        row_idx = 0
        col_idx = 0
        for i in range(9):
            targ_r = board[i]
            nums_r = [n for n in targ_r if n != "."]
            nums_set_r = set(targ_r)
            nums_set_r.remove(".")
            row.append(len(nums_r) == len(nums_set_r))

            targ_c = [row[i] for row in board]
            nums_c = [n for n in targ_c if n != "."]
            nums_set_c = set(targ_c)
            nums_set_c.remove(".")
            col.append(len(nums_c) == len(nums_set_c))

            if i % 3 == 0 and i > 0:
                row_idx += 3
                col_idx = 0
            targ_sq = []
            for x in range(3):
                targ_sq.extend(board[row_idx+x][col_idx:col_idx+3])
            col_idx += 3

            nums_sq = [n for n in targ_sq if n != "."]
            nums_set_sq = set(targ_sq)
            nums_set_sq.remove(".")
            sq.append(len(nums_sq) == len(nums_set_sq))
            
            

        print(sum(sq))
        print(sum(row))
        print(sum(col))
        return sum(row) == sum(col) == sum(sq) == 9
