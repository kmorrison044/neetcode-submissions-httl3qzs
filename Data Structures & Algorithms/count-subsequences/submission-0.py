class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        memo = [[-1] * nt for _ in range(ns)]
        
        def dfs(i, j):
            if j == nt:
                return 1
            if i == ns:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            if s[i] == t[j]:
                memo[i][j] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[i][j] = dfs(i + 1, j)
            
            return memo[i][j]
        
        return dfs(0, 0)
