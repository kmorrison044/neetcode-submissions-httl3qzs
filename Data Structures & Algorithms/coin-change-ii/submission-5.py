class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # Create a matrix that stores all the possible current amounts (i.e 0 up to 
        # amount, which is why we add 1 to amount. These are the columns) vs all
        # the different choices we have for coins (rows). We also add 1 to n for the
        # rows to prevent index out of bounds errors and represent what happens when 
        # we run out of coins.
        tab = [[0] * (amount + 1) for _ in range(n + 1)]

        # This sets the base case. When the current value == amount, then we know
        # that we have found 1 way to make change for the amount.
        for i in range(n + 1):
            tab[i][amount] = 1

        # Iterate backward through the matrix
        for i in range(n - 1, -1, -1):
            for curr in range(amount - 1, -1, -1):
                # The current state of the tab matrix is equal to the value we get
                # if we take the current coin (curr + coins[i]) vs not taking the coin
                # (i + 1). When we take the current coin, we don't increment i, since we
                # can choose it multiple times.
                tab[i][curr] = (tab[i][curr + coins[i]] if curr + coins[i] <= amount else 0) + tab[i + 1][curr]

        # Return the first value of the list, where curr = 0 and i = 0 
        # (i.e. the beginning of the coins list).
        return tab[0][0]