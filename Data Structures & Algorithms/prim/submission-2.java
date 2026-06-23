class Solution {
    public int minimumSpanningTree(List<List<Integer>> edges, int n) {
        Map<Integer, List<int[]>> adj = new HashMap<>();
        Set<Integer> visit = new HashSet<>();
        Queue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        for (List<Integer> edge : edges)
        {
            int u = edge.get(0);
            int v = edge.get(1);
            int w = edge.get(2);

            adj.computeIfAbsent(u, k -> new ArrayList<int[]>()).add(new int[]{w, v});
            adj.computeIfAbsent(v, k -> new ArrayList<int[]>()).add(new int[]{w, u});
        }

        q.offer(new int[]{0, 0});
        int res = 0;

        while (!q.isEmpty() && visit.size() < n)
        {
            int[] data = q.poll();
            int w = data[0], node = data[1];

            if (visit.contains(node))
            {
                continue;
            }

            visit.add(node);
            res += w;

            for (int[] neighbor : adj.getOrDefault(node, new ArrayList<>()))
            {
                int new_weight = neighbor[0];
                int nei = neighbor[1];
                if (!visit.contains(nei))
                {
                    q.offer(new int[]{new_weight, nei});
                }
            }
        }

        return visit.size() < n ? -1 : res;
    }
}    
