class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = n;
        while (true)
        {
            fast = sumOfSquares(fast);
            fast = sumOfSquares(fast);
            slow = sumOfSquares(slow);
            if (slow == fast)
            {
                break;
            }
        }

        int slow2 = n;
        while (slow != slow2)
        {
            slow = sumOfSquares(slow);
            slow2 = sumOfSquares(slow2);
        }

        return slow == 1 ? true : false;
    }

    public int sumOfSquares(int num)
    {
        int output = 0;

        while (num != 0)
        {
            int digit = num % 10;
            output += Math.pow(digit, 2);
            num /= 10;
        }

        return output;
    }
}
