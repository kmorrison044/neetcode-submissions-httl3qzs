class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        tab = [[0] * (amount + 1) for _ in range(n + 1)]
        if amount == 0:
            return 1

        for i in range(n - 1, -1, -1):
            for curr in range(amount - 1, -1, -1):
                if curr + coins[i] == amount:
                    tab[i][curr] = 1 + tab[i + 1][curr]
                else:
                    tab[i][curr] = (tab[i][curr + coins[i]] if curr + coins[i] <= amount else 0) + tab[i + 1][curr]

        return tab[0][0]