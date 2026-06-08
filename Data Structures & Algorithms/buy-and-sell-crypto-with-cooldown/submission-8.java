class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] tab = new int[prices.length + 1][2];

        for (var i = n - 1; i >= 0; i--)
        {
            for (var buying : List.of(true, false))
            {
                var buyingIdx = buying ? 1 : 0;
                var cooldown = i + 1 >= n ? 0 : tab[i + 1][buyingIdx];
                if (buying)
                {
                    var buy = i + 1 >= n ? -prices[i] : tab[i + 1][0] - prices[i];
                    tab[i][buyingIdx] = Math.max(buy, cooldown);
                }
                else
                {
                    var sell = i + 1 >= n ? prices[i] : tab[i + 2][1] + prices[i];
                    tab[i][buyingIdx] = Math.max(sell, cooldown);
                }
            }
        }
        return tab[0][1];
    }
}
