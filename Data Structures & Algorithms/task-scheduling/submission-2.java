class Solution {
    public int leastInterval(char[] tasks, int n) {
        int time = 0;
        Map<Character, Integer> count = new HashMap<>();
        Queue<int[]> q = new ArrayDeque<>();
        Queue<Integer> h = new PriorityQueue<>((a, b) ->
            Integer.compare(b, a)
        );

        for (char c : tasks)
        {
            // count.put(c, count.getOrDefault(c, 0) + 1);
            count.compute(c, (key, val) -> (val == null) ? 1 : val + 1);
        }

        count.forEach((k, v) -> {
            h.offer(v);
        });

        while (!q.isEmpty() || !h.isEmpty())
        {
            time++;

            if (!h.isEmpty())
            {
                int cnt = h.poll() - 1;
                if (cnt != 0)
                {
                    q.offer(new int[] {cnt, time + n});
                }
            }

            if (!q.isEmpty() && q.peek()[1] == time)
            {
                h.offer(q.poll()[0]);
            }
        }

        return time;
    }
}
