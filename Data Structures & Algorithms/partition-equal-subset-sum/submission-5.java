class Solution {
    public boolean canPartition(int[] nums) {
        int total = Arrays.stream(nums).sum();

        if (total % 2 != 0) return false;

        int n = nums.length;
        int target = total / 2;
        Set<Integer> dp = new HashSet<>();
        dp.add(0);

        for (int i = n - 1; i >= 0; i--)
        {
            Set<Integer> temp = new HashSet<>();
            int num = nums[i];

            for (int t : dp)
            {
                temp.add(num + t);
                temp.add(t);

                if (temp.contains(target))
                {
                    return true;
                }
            }

            dp = temp;
        }

        return false;
    }
}
