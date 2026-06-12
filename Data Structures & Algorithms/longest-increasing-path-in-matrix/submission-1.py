class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        memo = [[-1] * m for _ in range(n)]
        
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]

            cell = matrix[i][j]
            p1 = 1 + dfs(i - 1, j) if i - 1 >= 0 and matrix[i - 1][j] > cell else 1
            p2 = 1 + dfs(i + 1, j) if i + 1 < n and matrix[i + 1][j] > cell else 1
            p3 = 1 + dfs(i, j - 1) if j - 1 >= 0 and matrix[i][j - 1] > cell else 1
            p4 = 1 + dfs(i, j + 1) if j + 1 < m and matrix[i][j + 1] > cell else 1

            memo[i][j] = max(p1, p2, p3, p4)
            return memo[i][j]
        
        ret = 0
        for i in range(n):
            for j in range(m):
                # memo = [[-1] * m for _ in range(n)]
                ret = max(ret, dfs(i, j))

        return ret