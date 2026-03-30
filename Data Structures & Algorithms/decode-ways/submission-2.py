class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n : 1}
        res = 0

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if (i < n - 1 and (s[i] == '1' or s[i] == '2' and int(s[i + 1]) < 7)):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)
