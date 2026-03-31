class Solution {
    public int coinChange(int[] coins, int amount) {
        double[] memo = new double[amount + 1];
        Arrays.fill(memo, Double.POSITIVE_INFINITY);
        memo[0] = 0;

        for (int i = 1; i < memo.length; i++)
        {
            for (int c : coins)
            {
                if (i - c >= 0)
                {
                    memo[i] = Math.min(memo[i], 1 + memo[i - c]);
                }
            }
        }

        return memo[amount] == Double.POSITIVE_INFINITY ? -1 : (int) memo[amount];
    }
}
