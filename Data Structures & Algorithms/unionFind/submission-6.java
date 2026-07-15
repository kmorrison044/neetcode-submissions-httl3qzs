class UnionFind {
    private int[] parent;
    private int[] size;
    private int comps;

    public UnionFind(int n) {
        this.parent = new int[n];
        this.size = new int[n];
        this.comps = n;

        for (int i = 0; i < n; i++)
        {
            this.parent[i] = i;
        }
    }

    public int find(int x) {
        if (x != this.parent[x])
        {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    public boolean isSameComponent(int x, int y) {
        return this.find(x) == this.find(y);
    }

    public boolean union(int x, int y) {
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

    public int getNumComponents() {
        return this.comps;
    }
}
