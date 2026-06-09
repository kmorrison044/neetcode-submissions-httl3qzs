class Solution {
    public int change(int amount, int[] coins) {
        int n = coins.length;
        int [][] tab = new int [n + 1][amount + 1];

        for (int i = 0; i < n + 1; i++)
        {
            tab[i][amount] = 1;
        }

        for (int i = n - 1; i >= 0; i--)
        {
            for (int curr = amount; curr >= 0; curr--)
            {
                var take_coin = 0;
                if (curr + coins[i] <= amount)
                {
                    take_coin = tab[i][curr + coins[i]];
                }

                var skip_coin = tab[i + 1][curr];

                tab[i][curr] = take_coin + skip_coin;
            }
        }

        return tab[0][0];
    }
}
