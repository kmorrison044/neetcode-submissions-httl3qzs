class Solution {
    private int cycleStart = -1;
    private Set<Integer> cycle = new HashSet<>();
    private Set<Integer> visited = new HashSet<>();
    private Map<Integer, List<Integer>> adj = new HashMap<>();

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        for (int i = 0; i <= n; i++)
        {
            adj.put(i, new ArrayList<Integer>());
        }

        for (int[] pair : edges)
        {
            adj.get(pair[0]).add(pair[1]);
            adj.get(pair[1]).add(pair[0]);
        }

        dfs(1, -1);

        for (int i = n - 1; i >= 0; i--)
        {
            int[] pair = edges[i];
            if (cycle.contains(pair[0]) && cycle.contains(pair[1]))
            {
                return new int[] {pair[0], pair[1]};
            }
        }
        
        return new int[0];
    }

    public boolean dfs(int node, int par)
    {
        if (visited.contains(node))
        {
            cycleStart = node;
            return true;
        }

        visited.add(node);
        for (int nei : adj.get(node))
        {
            if (nei == par)
            {
                continue;
            }
            if (dfs(nei, node))
            {
                if (cycleStart != -1)
                {
                    cycle.add(node);
                }
                if (cycleStart == node)
                {
                    cycleStart = -1;
                }
                return true;
            }
        }
        return false;
    }
}
