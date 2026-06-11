class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        memo = [[-1] * (n2 + 1) for _ in range(n1 + 1)]

        def dfs(i, j):
            if i == n1 and j == n2 and i + j == n3:
                return True
            
            if i < n1 and j < n2 and memo[i][j] != -1:
                return memo[i][j]
            
            match_s1 = False
            match_s2 = False
            if j < n2 and i + j < n3 and s2[j] == s3[i + j]:
                match_s1 = dfs(i, j + 1)
            if i < n1 and i + j < n3 and s1[i] == s3[i + j]:
                match_s2 = dfs(i + 1, j) 

            memo[i][j] = match_s1 or match_s2
            return memo[i][j]
        
        return dfs(0, 0)