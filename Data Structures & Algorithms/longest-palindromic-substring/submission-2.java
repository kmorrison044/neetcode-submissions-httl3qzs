class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int idx = 0, len = 0;
        boolean[][] memo = new boolean[n][n];

        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = i; j < n; j++)
            {
                if (s.charAt(i) == (s.charAt(j)) && (j - i <= 2 || memo[i + 1][j - 1] == true))
                {
                    memo[i][j] = true;
                    if (j - i + 1 > len)
                    {
                        len = j - i + 1;
                        idx = i;
                    }
                }
            }
        }

        return s.substring(idx, idx + len);
    }
}
