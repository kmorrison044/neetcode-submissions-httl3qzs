class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> adj = new HashMap<>();
        Queue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        Set<Integer> visit = new HashSet<>();

        for (int[] time: times)
        {
            var s = time[0];
            var e = time[1];
            var t = time[2];

            adj.computeIfAbsent(s, key -> new ArrayList<>()).add(new int[]{e, t});
        }

        int INF = 1_000_000_000;
        int NEG_INF = -1_000_000_000;

        int[] shortest = new int[n + 1];
        for (int i = 0; i < n + 1; i++)
        {
            shortest[i] = INF;
        }
        shortest[0] = NEG_INF;
        shortest[k] = 0;

        q.offer(new int[]{0, k});

        while(!q.isEmpty())
        {
            var data = q.poll();
            var curr_time = data[0];
            var node = data[1];

            if (curr_time > shortest[node])
            {
                continue;
            }

            visit.add(node);

             for (int[] nei_data : adj.getOrDefault(node, new ArrayList<>()))
             {
                var nei = nei_data[0];
                var edge_time = nei_data[1];

                var new_time = edge_time + curr_time;
                if (new_time < shortest[nei])
                {
                    shortest[nei] = new_time;
                    q.offer(new int[]{new_time, nei});
                }
             }
        }

        var minimum = NEG_INF;
        for (int i = 0; i < shortest.length; i++)
        {
            minimum = Math.max(minimum, shortest[i]);
        }

        return visit.size() == n ? minimum : -1;
    }
}