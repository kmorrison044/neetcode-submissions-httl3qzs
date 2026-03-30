class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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