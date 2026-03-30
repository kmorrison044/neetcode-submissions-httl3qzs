class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window problem. Set left pointer to initial element and right pointer to the second
        # element. Loop through the array until right >= len(prices). On each iteration, calculate 
        # current profit and max profit. If your left price is greater than your right price, that
        # means you found your lowest price, so set left = right. On every iteration update r.
        # r will eventually be >= len(prices) and break out of loop. The max profit var stores
        # max profit so return that var.
        l, r = 0, 1
        
        maxP = 0
        while r < len(prices):
            left = prices[l]
            right = prices[r]

            profit = right - left
            maxP = max(profit, maxP)
            if left > right:
                l = r
            
            r += 1

        return maxP