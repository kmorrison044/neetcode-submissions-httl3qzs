class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # This table tracks the current amount we have collected so far (columns) vs
        # what denomination we are at in the "coins" table.
        memo = [[-1] * (amount + 1) for _ in range(n)]

        # dfs tracking the current index and current amount collected.
        def dfs(i, curr):
            # If curr == amount, immediately return 1, since we have found 1 way to return change
            # for the amount of money.
            if curr == amount:
                return 1
            # If i is greater than the length of the coins list, or if the current amount we have
            # collected is greater than the target amount, return 0.
            if i >= n or curr > amount:
                return 0
            # Return the cached value if we already calculated it.
            if memo[i][curr] != -1:
                return memo[i][curr]
            
            # Store the result of the current state in the memo table to reduce recalculation
            # of the same problem.
            memo[i][curr] = dfs(i, curr + coins[i]) + dfs(i + 1, curr)
            # Return cached value
            return memo[i][curr]

        # Call and return value of initial dfs state.
        return dfs(0, 0)