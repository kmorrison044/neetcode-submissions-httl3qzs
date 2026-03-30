class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> q = new PriorityQueue<>();

        for (int n : nums)
        {
            q.offer(n);
            if (q.size() > k)
            {
                q.poll();
            }
        }

        return q.peek();
    }
}
