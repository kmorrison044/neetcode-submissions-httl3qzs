class Solution {
    private Set<List<Integer>> pac = new HashSet<>(), atl = new HashSet<>();

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        final int ROWS = heights.length, COLS = heights[0].length;
        List<List<Integer>> ret = new ArrayList<>();

        for (int r = 0; r < ROWS; r++)
        {
            dfs(r, COLS - 1, atl, heights);
            dfs(r, 0, pac, heights);
        }

        for (int c = 0; c < COLS; c++)
        {
            dfs(ROWS - 1, c, atl, heights);
            dfs(0, c, pac, heights);
        }

        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                if (pac.contains(List.of(r, c)) && atl.contains(List.of(r, c)))
                {
                    ret.add(Arrays.asList(r, c));
                }
            }
        }
        return ret;
    }

    public void dfs(int r, int c, Set<List<Integer>> visit, int[][] heights)
    {
        final int ROWS = heights.length, COLS = heights[0].length;

        if (visit.contains(List.of(r, c)))
        {
            return;
        }

        visit.add(List.of(r, c));
        if (r + 1 < ROWS && heights[r + 1][c] >= heights[r][c]) dfs(r + 1, c, visit, heights);
        if (r - 1 >= 0 && heights[r - 1][c] >= heights[r][c]) dfs(r - 1, c, visit, heights);
        if (c + 1 < COLS && heights[r][c + 1] >= heights[r][c]) dfs(r, c + 1, visit, heights);
        if (c - 1 >= 0 && heights[r][c - 1] >= heights[r][c]) dfs(r, c - 1, visit, heights);
    }
}
