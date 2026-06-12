class Solution {
    private int n, m;
    private int[][] memo;
    private int[][] matrix;

    public int longestIncreasingPath(int[][] matrix) {
        this.n = matrix.length;
        this.m = matrix[0].length;
        this.memo = new int[n][m];
        this.matrix = matrix;
        for (int[] row : this.memo)
        {
            Arrays.fill(row, -1);
        }

        var ret = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                ret = Math.max(ret, dfs(i, j));
            }
        }

        return ret;
    }

    public int dfs(int i, int j)
    {
        if (this.memo[i][j] != -1)
        {
            return this.memo[i][j];
        }

        var cell = this.matrix[i][j];
        var ret = 1;
        ret = (i + 1 < n && cell > this.matrix[i + 1][j]) ? Math.max(1 + dfs(i + 1, j), ret) : ret;
        ret = (i - 1 >= 0 && cell > this.matrix[i - 1][j]) ? Math.max(1 + dfs(i - 1, j), ret) : ret;
        ret = (j + 1 < m && cell > this.matrix[i][j + 1]) ? Math.max(1 + dfs(i, j + 1), ret) : ret;
        ret = (j - 1 >= 0 && cell > this.matrix[i][j - 1]) ? Math.max(1 + dfs(i, j - 1), ret) : ret;

        this.memo[i][j] = ret;
        return ret;
    }
}
