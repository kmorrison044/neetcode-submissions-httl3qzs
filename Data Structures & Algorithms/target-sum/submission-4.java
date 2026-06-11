class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int n = nums.length;
        int tot = Arrays.stream(nums).sum();

        if (Math.abs(target) > tot)
        {
            return 0;
        }

        int[][] tab = new int[nums.length + 1][tot * 2 + 1];
        tab[n][target + tot] = 1;

        for (int i = n - 1; i >= 0; i--)
        {
            for (int curr = -tot; curr < tot + 1; curr++)
            {
                int add = curr + nums[i];
                int sub = curr - nums[i];

                int future_add = (-tot <= add && add <= tot) ? tab[i + 1][add + tot] : 0;
                int future_sub = (-tot <= sub && sub <= tot) ? tab[i + 1][sub + tot] : 0;

                tab[i][curr + tot] = future_add + future_sub;
            }
        }

        return tab[0][0 + tot];
    }
}
