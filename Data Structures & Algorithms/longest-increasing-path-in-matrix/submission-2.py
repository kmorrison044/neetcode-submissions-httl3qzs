class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        # Memoize the results
        memo = [[-1] * m for _ in range(n)]
        
        def dfs(i, j):
            # if we got the value stored in the memo table,
            # return that to reduce compute.
            if memo[i][j] != -1:
                return memo[i][j]

            # Get the value of the current cell for comparison
            cell = matrix[i][j]
            # Run dfs in all 4 directions if the indices are valid and the next
            # position is strictly greater than the current cell. Otherwise, set
            # the value as 1 since the value of a path containing just 1 cell is 1.
            p1 = 1 + dfs(i - 1, j) if i - 1 >= 0 and matrix[i - 1][j] > cell else 1
            p2 = 1 + dfs(i + 1, j) if i + 1 < n and matrix[i + 1][j] > cell else 1
            p3 = 1 + dfs(i, j - 1) if j - 1 >= 0 and matrix[i][j - 1] > cell else 1
            p4 = 1 + dfs(i, j + 1) if j + 1 < m and matrix[i][j + 1] > cell else 1

            # Set the memo value to the max value of the above
            memo[i][j] = max(p1, p2, p3, p4)
            # Return the cached value at this state.
            return memo[i][j]
        
        # Since we are not given a starting coordinate, we need to loop through
        # every cell and run dfs on it as the starting position to find the longest
        # path
        ret = 0
        for i in range(n):
            for j in range(m):
                # We DO NOT have to reset our memo table here.
                # Because we run dfs at every cell, we found the longest
                # path to get to that cell in every direction, so if in 
                # another dfs call we hit that cell again, we've already stored
                # the longest path in every direction, so we can just return the
                # cached result.
                ret = max(ret, dfs(i, j))

        # Return the max val
        return ret