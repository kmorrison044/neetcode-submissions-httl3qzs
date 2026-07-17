class UnionFind
{
    private int[] parents;
    private int[] size;
    private int comps;

    public UnionFind(int n)
    {
        this.parents = new int[n];
        this.size = new int[n];
        this.comps = n;

        for (int i = 0; i < n; i++)
        {
            this.parents[i] = i;
        }
    }

    public int find(int x)
    {
        if (x != this.parents[x])
        {
            this.parents[x] = this.find(this.parents[x]);
        }
        return this.parents[x];
    }

    public boolean union(int x, int y)
    {
        var root_x = this.find(x);
        var root_y = this.find(y);

        if (root_x == root_y)
        {
            return false;
        }

        if (this.size[root_x] > this.size[root_y])
        {
            this.parents[root_y] = root_x;
            this.size[root_x] += this.size[root_y];
        }
        else
        {
            this.parents[root_x] = root_y;
            this.size[root_y] += this.size[root_x];
        }

        this.comps -= 1;
        return true;
    }
}

class Solution {
    private int manhattan(int[] a, int[] b)
    {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }

    public int minCostConnectPoints(int[][] points) {
        Queue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int n = points.length;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                var point1 = points[i];
                var point2 = points[j];
                var dist = this.manhattan(point1, point2);
                q.offer(new int[] {dist, i, j});
            }
        }

        UnionFind uf = new UnionFind(n);
        int res = 0;

        while (!q.isEmpty())
        {
            int[] data = q.poll();
            var dist = data[0];
            var u = data[1];
            var v = data[2];

            if (uf.union(u, v))
            {
                res += dist;
            }
        }

        return res;
    }
}
