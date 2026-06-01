class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[None] * 2 for _ in range(len(prices))]

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if memo[i][buying]:
                return memo[i][buying]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                memo[i][buying] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                memo[i][buying] = max(sell, cooldown)

            return memo[i][buying]
            
        return dfs(0, True)