class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1] * amount for _ in range(n)]

        def dfs(i, curr):
            if curr == amount:
                return 1
            if i >= n or curr > amount:
                return 0
            if memo[i][curr] != -1:
                return memo[i][curr]
            
            memo[i][curr] = dfs(i, curr + coins[i]) + dfs(i + 1, curr)
            return memo[i][curr]

        return dfs(0, 0)