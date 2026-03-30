class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int res1 = 1, res2 = 0;
        int temp = 0;

        for (int i = n - 1; i >= 0; i--)
        {
            if (s.charAt(i) == '0')
            {
                temp = 0;
            }
            else
            {
                temp = res1;
            }

            if (i < n - 1 && (s.charAt(i) == '1' || 
            s.charAt(i) == '2' && s.charAt(i + 1) - '0' < 7))
            {
                temp += res2;
            }

            res2 = res1;
            res1 = temp;
            temp = 0;
        }

        return res1;
    }
}
