class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        # Create memo table of every possible combo of pointers
        # between s and t
        memo = [[-1] * nt for _ in range(ns)]
        
        # Create dfs function that tracks pointers of s and t
        def dfs(i, j):
            # If we reach the end of t, that means we have 
            # fully matched it: return 1
            if j == nt:
                return 1
            # If we haven't reached the end of t, but we have reached
            # the end of s, then we didn't find a match: return 0
            if i == ns:
                return 0
            # Return cached results if we have them.
            if memo[i][j] != -1:
                return memo[i][j]
            
            # If the current value for s == t, then add the dfs calls
            # including that value and skipping that value, otherwise,
            # just skip the value
            memo[i][j] = (dfs(i + 1, j + 1) + dfs(i + 1, j)
                          if s[i] == t[j] else dfs(i + 1, j))

            # Return the calculated value
            return memo[i][j]
        
        # Call dfs at the start of both strings
        return dfs(0, 0)
