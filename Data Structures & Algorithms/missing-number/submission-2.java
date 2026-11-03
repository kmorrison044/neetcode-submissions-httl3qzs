class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int out = n;

        for (int i = 0; i < n; i++)
        {
            out ^= i ^ nums[i];
        }

        return out;
    }
}
