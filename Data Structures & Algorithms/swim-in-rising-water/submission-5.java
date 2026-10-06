class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        boolean[][] visit = new boolean[n][n];
        Queue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[][] directions = {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}
        };

        q.offer(new int[]{grid[0][0], 0, 0});
        visit[0][0] = true;

        while (!q.isEmpty())
        {
            int[] curr = q.poll();
            int t = curr[0], r = curr[1], c = curr[2];
            if (r == n - 1 && c == n - 1)
            {
                return t;
            }

            for (int[] dir : directions)
            {
                int neiR = r + dir[0], neiC = c + dir[1];
                if (neiR >= 0 && neiC >= 0 && neiR < n && neiC < n
                    && !visit[neiR][neiC])
                {
                    visit[neiR][neiC] = true;
                    q.offer(new int[]{Math.max(t, grid[neiR][neiC]), neiR, neiC});
                }
            }
        }
        throw new IllegalArgumentException("No valid path found to target destination");
    }
}
