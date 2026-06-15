class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        memo = [[-1] * (n2 + 1) for _ in range(n1 + 1)]

        def dfs(i, j):
            if i == n1 and j == n2:
                return 0
            if i > n1 or j > n2:
                return float('inf')
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            if i < n1 and j < n2 and word1[i] == word2[j]:
                memo[i][j] = dfs(i + 1, j + 1)
            else:
                # Replace
                o1 = 1 + dfs(i + 1, j + 1)
                # Delete
                o2 = 1 + dfs(i + 1, j)
                # Insert
                o3 = 1 + dfs(i, j + 1)
    
                memo[i][j] = min(o1, o2, o3)
            return memo[i][j]
        
        return dfs(0, 0)