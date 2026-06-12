class Solution {
    private int ns, nt;
    private int[][] memo;
    private String s, t;

    public int numDistinct(String s, String t) {
        this.s = s;
        this.t = t;
        this.ns = s.length();
        this.nt = t.length();
        this.memo = new int[ns][nt];

        for (int[] row : this.memo)
        {
            Arrays.fill(row, -1);
        }

        return dfs(0, 0);
    }

    public int dfs(int i, int j)
    {
        if (j == this.nt)
        {
            return 1;
        }
        if (i == this.ns)
        {
            return 0;
        }

        if (this.memo[i][j] != -1)
        {
            return this.memo[i][j];
        }

        this.memo[i][j] = dfs(i + 1, j);
        if (this.s.charAt(i) == this.t.charAt(j))
        {
            this.memo[i][j] += dfs(i + 1, j + 1);
        }
        
        return this.memo[i][j];
    }
}