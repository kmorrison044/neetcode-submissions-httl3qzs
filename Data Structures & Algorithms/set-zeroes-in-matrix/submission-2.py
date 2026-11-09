class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # We are going to use the first column and first row
        # to mark if anything in that row and column needs to be
        # set to zero
        rows, cols = len(matrix), len(matrix[0])
        # since the first row and column intersect, we need 1 more variable to 
        # determine if the first row needs to be set to zero
        firstRow = False

        # Iterate through the matrix to determine what rows and columns need to be
        # set to zero
        for r in range(rows):
            for c in range(cols):
                # if the current position is zero:
                if matrix[r][c] == 0:
                    # mark the current column as needing to be set to zero by marking
                    # the current column in the first row as zero
                    matrix[0][c] = 0

                    # Again since the first row and column overlap, if the current row is
                    # greater than zero, we can mark the first column in the current row as
                    # zero to indicate that the entire row needs to be set to zero.
                    if r > 0:
                        matrix[r][0] = 0
                    # Otherwise we set our first row boolean to true, indicating that the entire first
                    # row needs to be set to zero.
                    else:
                        firstRow = True
        
        # Now that we know all the rows and column to set to zero, iterate
        # through the matrix again, skipping the first row and column
        for r in range(1, rows):
            for c in range(1, cols):
                # If the current position falls in a row or column that needs to be marked
                # as zero, mark the current position as 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Now we handle if the first column needs to be set to zero by checking if the first
        # position is zero.
        if matrix[0][0] == 0:
            # if so, mark the whole column as zero
            for r in range(rows):
                matrix[r][0] = 0
        
        # If we determined the first row needs to be zeroed out
        if firstRow:
            # then mark the whole row as 0
            for c in range(cols):
                matrix[0][c] = 0