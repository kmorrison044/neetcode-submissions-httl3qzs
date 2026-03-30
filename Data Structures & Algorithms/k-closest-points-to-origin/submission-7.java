class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Use a priority q and a comparator to make it a max heap.
        // the inputs in the lambda are a (incumbent in the q) and b (the newcomer)
        // when doing q.offer(x). The priority queue only thinks the first integer
        // is smaller (higher priority) if the compare function returns -1, so when we
        // flip the inputs in the compare function, if b is bigger, it will return 1, so 
        // the q will take the second number as the "smaller one" (higher priority), but 
        // the second number in the input is b, which is actually the larger one.
        Queue<int []> q = new PriorityQueue<>((a, b) -> Integer.compare(
            (b[0] * b[0] + b[1] * b[1]), (a[0] * a[0] + a[1] * a[1]))
        );

        for (int[] point : points)
        {
            q.offer(point);
            if (q.size() > k)
            {
                q.poll();
            }
        }

        int[][] ret = new int[k][2];
        while (k > 0)
        {
            // if k = 3, then the indexes should be 2, 1, 0
            // --k means to update the value first, then use it,
            // so when using it as an index, it is immediately 2 instead
            // of 3.
            ret[--k] = q.poll();
        }

        return ret;
    }
}
