class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        int n = hand.length;
        Map<Integer, Integer> count = new HashMap<>();
        if (n % groupSize != 0)
        {
            return false;
        }

        for (int num : hand)
        {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        for (int num : hand)
        {
            var start = num;
            while (count.getOrDefault(start - 1, 0) > 0)
            {
                start--;
            }

            while(count.getOrDefault(start, 0) > 0)
            {
                for (int i = start; i < start + groupSize; i++)
                {
                    if (count.getOrDefault(i, 0) <= 0)
                    {
                        return false;
                    }

                    count.put(i, count.get(i) - 1);
                }
            }
        }

        return true;
    }
}
