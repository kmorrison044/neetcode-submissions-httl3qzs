class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create memo table for each possibility of text1 and text2 positions
        memo = [len(text2) * [-1] for _ in range(len(text1))]

        # Recursively go through and compare each position of the texts
        def dfs(i, j):
            # Check if indices are inbounds
            if i >= len(text1) or j >= len(text2):
                return 0
            # If texts are equal, set memo table and continue to recurse
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dfs(i + 1, j + 1)
                return memo[i][j]
            # If text are not equal, check if memo table has a value for the current positions
            if memo[i][j] != -1:
                return memo[i][j]
            
            # Otherwise, set the current position's value in the memo table equal to the
            # max value of the recursion between incrementing text1's pointer and leaving text2's
            # pointer the same and vice-versa
            memo[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            # Return the value of the current position
            return memo[i][j]
        
        return dfs(0, 0)