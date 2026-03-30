class Solution {
    public int rob(int[] nums) {
        return (nums.length == 1 ? nums[0] : Math.max(nums[0], 
        Math.max(helper(nums, 0), helper(nums, nums.length - 1))));
    }

    public int helper(int[] nums, int skip)
    {
        int rob1 = 0, rob2 = 0;
        for (int i = 0; i < nums.length; i++)
        {
            if (i == skip)
            {
                continue;
            }

            int temp = Math.max(nums[i] + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }

        return rob2;
    }
}
