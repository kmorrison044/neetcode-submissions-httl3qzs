class Solution {
    private record MajorityHolder(int count, Integer el) {};

    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        MajorityHolder maj = new MajorityHolder(Integer.MIN_VALUE, null);

        for (int n : nums)
        {
            int curr = counts.getOrDefault(n, 0) + 1;
            counts.put(n, curr);

            if (curr > maj.count())
            {
                maj = new MajorityHolder (curr, n);
            }
        }

        return maj.el();
    }
}