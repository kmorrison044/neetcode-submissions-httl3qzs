class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    memo[i] = min(memo[i], 1 + memo[i - c])
        return memo[amount] if memo[amount] != float('inf') else -1