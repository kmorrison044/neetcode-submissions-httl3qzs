class Solution {
    private String word1, word2;
    private Integer[][] memo;
    private int n1, n2;

    public int minDistance(String word1, String word2) {
        this.word1 = word1;
        this.word2 = word2;
        this.n1 = word1.length();
        this.n2 = word2.length();
        this.memo = new Integer[this.n1 + 1][this.n2 + 1];
        for (Integer[] row : this.memo)
        {
            Arrays.fill(row, null);
        }

        return dfs(0, 0);
    }

    public int dfs(int i, int j)
    {
        if (i == this.n1)
        {
            return this.n2 - j;
        }
        if (j == this.n2)
        {
            return this.n1 - i;
        }

        if (this.memo[i][j] != null)
        {
            return this.memo[i][j];
        }

        if (this.word1.charAt(i) == this.word2.charAt(j))
        {
            this.memo[i][j] = dfs(i + 1, j + 1);
        }
        else
        {
            var o1 = 1 + dfs(i + 1, j);
            var o2 = 1 + dfs(i + 1, j + 1);
            var o3 = 1 + dfs(i, j + 1);

            this.memo[i][j] = Math.min(o1, Math.min(o2, o3));
        }
        return this.memo[i][j];
    }
}
