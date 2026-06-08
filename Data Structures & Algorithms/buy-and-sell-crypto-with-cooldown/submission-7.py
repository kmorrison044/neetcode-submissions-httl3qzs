class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # The table is two columns that represent either buying or selling,
        # and the rows are the number of items in prices, plus an extra row
        # for base case.
        tab = [[0] * 2 for _ in range(n + 1)]

        # Iterate backwards through the whole matrix
        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                # You have the option everytime to cooldown, so go ahead and
                # calculate this value
                cooldown = tab[i + 1][buying] if i + 1 < n else 0
                # If you have the option to buy, calculate the difference between
                # the future price and the current price to find the profit with
                # the base case in mind
                if buying:
                    buy = tab[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    # The value for the current profit for the day is the max between
                    # choosing to buy vs choosing to cooldown
                    tab[i][1] = max(buy, cooldown)
                # If you have to sell, add the current price with the future profit you
                # can receive with future decisions, keeping the base case in mind.
                else:
                    # Must do i + 2 because of required cooldown.
                    sell = tab[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    # The value for the current profit for the day is the max between
                    # choosing to sell or cooldown.
                    tab[i][0] = max(sell, cooldown)

        # Return the first row and buying column since you must have the option to
        # buy starting out.
        return tab[0][1]