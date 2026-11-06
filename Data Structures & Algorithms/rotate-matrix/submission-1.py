class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # First transpose the matrix, which makes all the rows columns
        # and columns rows. This maintains order, so row 1 will be column
        # 1, and row 2 will be column 2, etc.
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Next, reverse each row of the matrix to complete the 89 degree
        # rotation.
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1