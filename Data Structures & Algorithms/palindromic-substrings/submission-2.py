class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        memo = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                    memo[i][j] = True
                    res += 1
        
        return res