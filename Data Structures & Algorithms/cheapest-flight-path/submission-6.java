class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Queue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        Map<Integer, List<int[]>> adj = new HashMap<>();
        Map<Integer, Integer> best_stops = new HashMap<>();

        for (int[] flight : flights)
        {
            int frm = flight[0], to = flight[1], price = flight[2];
            adj.computeIfAbsent(frm, e -> new ArrayList<>()).add(new int[]{to, price});
        }

        q.offer(new int[]{0, src, 0});
        while (!q.isEmpty())
        {
            int[] data = q.poll();
            int cost = data[0], node = data[1], stops = data[2];

            if (node == dst)
            {
                return cost;
            }
            if (stops > k || stops >= best_stops.getOrDefault(node, Integer.MAX_VALUE))
            {
                continue;
            }

            best_stops.put(node, stops);
            for (int[] nei_data : adj.getOrDefault(node, new ArrayList<>()))
            {
                int nei = nei_data[0], price = nei_data[1];
                q.offer(new int[]{price + cost, nei, stops + 1});
            }
        }

        return -1;
    }
}
