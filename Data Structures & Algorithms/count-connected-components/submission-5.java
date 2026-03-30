class Solution {
    private Set<Integer> visited = new HashSet<>();
    private Map<Integer, List<Integer>> adj = new HashMap<>();

    public int countComponents(int n, int[][] edges) {
        int count = 0;

        for (int i = 0; i < n; i++)
        {
            adj.put(i, new ArrayList<Integer>());
        }

        for (int[] edge : edges)
        {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        for (int node = 0; node < n; node++)
        {
            if (!visited.contains(node))
            {
                bfs(node);
                count++;
            }
        }

        return count;
    }

    private void bfs(int node)
    {
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(node);
        visited.add(node);
        while (!q.isEmpty())
        {
            int curr = q.poll();
            for (int nei : adj.get(curr))
            {
                if (!visited.contains(nei))
                {
                    q.offer(nei);
                    visited.add(nei);
                }
            }
        }
    }
}
