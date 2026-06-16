class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)

        # Create a matrix the size of the two strings plus 1 in case
        # we finish one iterator before another.
        memo = [[-1 for _ in range(np + 1)] for _ in range(ns + 1)]

        def dfs(i, j):
            # If we reach the end of our regex pattern, check if we
            # are at the end of the string we are trying to match
            if j == np:
                return i == ns
            # Return cached results
            if memo[i][j] != -1:
                return memo[i][j]
            
            # Easiest to just store a variable to determine if the current
            # pointers are matching
            match = i < ns and (s[i] == p[j] or p[j] == '.')
            # First check the wildcard case because if the following pointer is
            # a wildcard, then the current pointers will obviously match as well.
            if j + 1 < np and p[j + 1] == '*':
                # Since the wildcard can match 0 or more times of the preceding character,
                # then check the result if we just skipped it, or if it matches the current
                # character, then increment just i on the dfs. Once we run out of matches on
                # j, we will skip it according to the first call again.
                memo[i][j] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            # If no wildcard character, just check a strict match and increment the
            # pointers.
            elif match:
                memo[i][j] = dfs(i + 1, j + 1)
            else:
                # False if the above is false
                memo[i][j] = False
            
            return memo[i][j]
        
        return dfs(0, 0)