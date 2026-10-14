class Solution {
    private Map<Integer, List<Integer>> adj;
    private Map<Integer, Boolean> visited;
    private List<Integer> ret;

    public List<Integer> topologicalSort(int n, int[][] edges) {
        adj = new HashMap<>();
        visited = new HashMap<>();
        ret = new ArrayList<>();

        for (int[] edge : edges)
        {
            int u = edge[0], v = edge[1];
            adj.computeIfAbsent(u, k -> new ArrayList<Integer>()).add(v);
        }

        for (int i = 0; i < n; i++)
        {
            if (!dfs(i))
            {
                return new ArrayList<>();
            }
        }

        return ret.reversed();
    }

    public Boolean dfs(int node)
    {
        if (visited.containsKey(node))
        {
            return !visited.get(node);
        }

        visited.put(node, true);

        for (Integer nei : adj.getOrDefault(node, new ArrayList<Integer>()))
        {
            if (!dfs(nei))
            {
                return false;
            }
        }

        visited.put(node, false);
        ret.add(node);
        return true;
    }
}
