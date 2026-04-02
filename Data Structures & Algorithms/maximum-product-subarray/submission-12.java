class Solution {
    public int maxProduct(int[] nums) {
        int currMin = 1, currMax = 1;
        int res = nums[0];

        for (int n : nums)
        {
            int tmp = currMax;
            currMax = Math.max(n, Math.max(n * currMin, n * currMax));
            currMin = Math.min(n, Math.min(n * currMin, n * tmp));
            res = Math.max(res, currMax);
        }

        return res;
    }
}
