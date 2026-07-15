class UnionFind {
    private int[] parent;
    private int[] size;
    private Integer comps;

    public UnionFind(int n) {
        this.parent = new int[n];
        this.size = new int[n];
        this.comps = n;

        for (int i = 0; i < n; i++)
        {
            this.parent[i] = i;
        }
    }

    public int find(int x)
    {
        if (x != this.parent[x])
        {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    public int getNumComponents()
    {
        return this.comps;
    }

    public boolean union(int x, int y)
    {
        int root_x = this.find(x);
        int root_y = this.find(y);

        if (root_x == root_y)
        {
            return false;
        }

        if (this.size[root_x] > this.size[root_y])
        {
            this.parent[root_y] = root_x;
            this.size[root_x] += this.size[root_y];
        }
        else
        {
            this.parent[root_x] = root_y;
            this.size[root_y] += this.size[root_x];
        }

        this.comps -= 1;
        return true;
    }
}

class Solution {
    public int minimumSpanningTree(List<List<Integer>> edges, int n) {
        Queue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        for (List<Integer> edge : edges)
        {
            int u = edge.get(0);
            int v = edge.get(1);
            int w = edge.get(2);

            q.offer(new int[]{w, u, v});
        }

        var uf = new UnionFind(n);
        int res = 0;
        while (!q.isEmpty())
        {
            int[] edge = q.poll();
            int w = edge[0];
            int u = edge[1];
            int v = edge[2];

            if (uf.union(u, v))
            {
                res += w;
            }
        }

        return uf.getNumComponents() == 1 ? res : -1;
    }
}
