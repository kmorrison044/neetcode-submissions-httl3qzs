class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [len(text2) * [-1] for _ in range(len(text1))]

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dfs(i + 1, j + 1)
                return memo[i][j]
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[i][j]
        
        return dfs(0, 0)