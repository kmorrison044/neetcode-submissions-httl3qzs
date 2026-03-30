class Solution {
    public boolean validTree(int n, int[][] edges) {
        Set<Integer> visited = new HashSet<>();
        Map<Integer, List<Integer>> adj = new HashMap<>();
        Queue<int []> q = new ArrayDeque<>();

        for (int node = 0; node < n; node++)
        {
            adj.put(node, new ArrayList<Integer>());
        }

        for (int[] pair : edges)
        {
            adj.get(pair[0]).add(pair[1]);
            adj.get(pair[1]).add(pair[0]);
        }

        q.offer(new int[] {0, -1});
        visited.add(0);

        while (!q.isEmpty())
        {
            int size = q.size();
            for (int i = 0; i < size; i++)
            {
                int[] pair = q.poll();
                int node = pair[0], par = pair[1];

                for (int nei : adj.get(node))
                {
                    if (nei == par)
                    {
                        continue;
                    }
                    if (visited.contains(nei))
                    {
                        return false;
                    }
                    visited.add(nei);
                    q.offer(new int[] {nei, node});
                }
            }
        }
        return visited.size() == n;
    }
}
