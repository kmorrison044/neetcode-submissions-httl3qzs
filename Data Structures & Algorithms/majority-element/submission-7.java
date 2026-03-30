class Solution {
    public int majorityElement(int[] nums) {
        Integer cand = null;
        int count = 0;

        for (int n : nums)
        {
            if (count == 0)
            {
                cand = n;
            }

            count += (cand == n) ? 1 : -1;
        }

        return cand;
    }
}