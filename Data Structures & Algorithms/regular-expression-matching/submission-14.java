class Solution {
    private String s, p;
    private Boolean[][] memo;
    private int ns, np;

    public boolean isMatch(String s, String p) {
        this.s = s;
        this.p = p;
        this.ns = s.length();
        this.np = p.length();
        this.memo = new Boolean[ns + 1][np + 1];
        for (Boolean[] row : this.memo)
        {
            Arrays.fill(row, null);
        }

        return dfs(0, 0);
    }

    public boolean dfs(int i, int j)
    {
        if (j == this.np)
        {
            return i == this.ns;
        }
        if (this.memo[i][j] != null)
        {
            return this.memo[i][j];
        }

        boolean match = ((i < this.ns) && 
                        (this.s.charAt(i) == this.p.charAt(j) || this.p.charAt(j) == '.'));
        
        if (j + 1 < this.np && this.p.charAt(j + 1) == '*')
        {
            this.memo[i][j] = (dfs(i, j + 2) || (match && dfs(i + 1, j)));
        }
        else if (match)
        {
            this.memo[i][j] = dfs(i + 1, j + 1);
        }
        else
        {
            this.memo[i][j] = false;
        }

        return this.memo[i][j];
    }
}
