class Solution {
    public int lastStoneWeight(int[] stones) {
        Queue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());

        for (int s : stones)
        {
            q.offer(s);
        }

        while (q.size() > 1)
        {
            int x = q.poll();
            int y = q.poll();

            int new_weight = Math.max(x, y) - Math.min(x, y);
            if (new_weight != 0)
            {
                q.offer(new_weight);
            }
        }

        return q.size() > 0 ? q.peek() : 0;
    }
}
