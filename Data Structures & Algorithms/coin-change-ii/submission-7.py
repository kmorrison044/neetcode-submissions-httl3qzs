class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        tab = [0] * (amount + 1)
        tab[amount] = 1

        for i in range(n - 1, -1, -1):
            next_row = [0] * (amount + 1)
            next_row[amount] = 1

            for curr in range(amount - 1, -1, -1):
                next_row[curr] = (tab[curr] + (next_row[curr + coins[i]] 
                                  if curr + coins[i] <= amount else 0))

            tab = next_row
        
        return tab[0]