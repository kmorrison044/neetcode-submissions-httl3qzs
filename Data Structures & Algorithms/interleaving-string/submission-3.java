class Solution {
    private String s1, s2, s3;
    private int n1, n2, n3;
    private Boolean[][] memo;

    public boolean isInterleave(String s1, String s2, String s3) {
        this.n1 = s1.length();
        this.n2 = s2.length();
        this.n3 = s3.length();

        this.s1 = s1;
        this.s2 = s2;
        this.s3 = s3;

        this.memo = new Boolean[n1 + 1][n2 + 1];

        if (n1 + n2 != n3)
        {
            return false;
        }

        return dfs(0, 0);
    }

    public boolean dfs(int i, int j)
    {
        if (i == this.n1 && j == this.n2 && i + j == this.n3)
        {
            return true;
        }

        if (this.memo[i][j] != null)
        {
            return this.memo[i][j];
        }

        boolean match_s1 = false;
        boolean match_s2 = false;
        if (i < n1 && this.s1.charAt(i) == this.s3.charAt(i + j))
        {
            match_s1 = dfs(i + 1, j);
        }
        if (j < n2 && this.s2.charAt(j) == this.s3.charAt(i + j))
        {
            match_s2 = dfs(i, j + 1);
        }

        this.memo[i][j] = match_s1 || match_s2;
        return this.memo[i][j];
    }
}
