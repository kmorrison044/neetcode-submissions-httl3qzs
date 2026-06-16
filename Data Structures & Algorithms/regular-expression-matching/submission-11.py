class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)

        memo = [[-1 for _ in range(np + 1)] for _ in range(ns + 1)]

        def dfs(i, j):
            if j == np:
                return i == ns
            if memo[i][j] != -1:
                return memo[i][j]
            
            match = i < ns and (s[i] == p[j] or p[j] == '.')
            if j + 1 < np and p[j + 1] == '*':
                memo[i][j] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                memo[i][j] = dfs(i + 1, j + 1)
            else:
                memo[i][j] = False
            
            return memo[i][j]
        
        return dfs(0, 0)