class Solution {
    public boolean isHappy(int n) {
        Set<Integer> m = new HashSet<>();
        int num = n;

        while (true)
        {
            int summation = 0;
            while (num != 0)
            {
                int digit = num % 10;
                num /= 10;
                summation += Math.pow(digit, 2);
            }

            if (m.contains(summation))
            {
                return false;
            }
            if (summation == 1)
            {
                return true;
            }

            m.add(summation);
            num = summation;
        }
    }
}
