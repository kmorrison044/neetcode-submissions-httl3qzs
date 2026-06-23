class Solution {
    public Map<Integer, Integer> shortestPath(int n, List<List<Integer>> edges, int src) {
        Queue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for (List<Integer> edge : edges)
        {
            int u = edge.get(0);
            int v = edge.get(1);
            int w = edge.get(2);

            adj.computeIfAbsent(u, k -> new ArrayList<int[]>()).add(new int[]{w, v});
        }

        Map<Integer, Integer> shortest = new HashMap<>();
        q.offer(new int[]{0, src});

        while (!q.isEmpty())
        {
            int[] data = q.poll();
            int node = data[1];
            int curr_dist = data[0];

            if (shortest.containsKey(node))
            {
                continue;
            }
            shortest.put(node, curr_dist);

            for (int[] nei : adj.getOrDefault(node, new ArrayList<>()))
            {
                int new_dist = nei[0] + curr_dist;
                if (!shortest.containsKey(nei[1]))
                {
                    q.offer(new int[]{new_dist, nei[1]});
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            shortest.computeIfAbsent(i, k -> -1);
        }

        return shortest;
    }  
}
