class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        idx, length = 0, 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                    memo[i][j] = True
                    if length < (j - i + 1):
                        idx = i
                        length = j - i + 1
        
        return s[idx :  idx + length]