class Solution {
    private List<String> res = new ArrayList<>();
    private Map<String, PriorityQueue<String>> adj = new HashMap<>();

    public List<String> findItinerary(List<List<String>> tickets) {
        for (List<String> ticket : tickets)
        {
            String src = ticket.get(0);
            String dst = ticket.get(1);

            this.adj.computeIfAbsent(src, k -> new PriorityQueue<>()).offer(dst);
        }

        dfs("JFK");
        Collections.reverse(res);
        return res;
    }

    public void dfs(String node)
    {
        PriorityQueue<String> q = adj.getOrDefault(node, new PriorityQueue<>());
        while (!q.isEmpty())
        {
            String dst = q.poll();
            dfs(dst);
        }
        res.add(node);
    }
}
