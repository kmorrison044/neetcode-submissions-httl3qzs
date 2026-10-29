class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        Queue<int[]> priQ = new PriorityQueue<>(Comparator.comparingInt((int[] a) -> a[0])
                                                        .thenComparingInt(a -> a[1]));
        Arrays.sort(intervals, Comparator.comparingInt((int[] x) -> x[0])
                                        .thenComparingInt(x -> x[1]));
        Map<Integer, Integer> res = new HashMap<>();
        int i = 0;

        for (int q : Arrays.stream(queries).sorted().toArray())
        {
            while (i < intervals.length && q >= intervals[i][0])
            {
                int l = intervals[i][0], r = intervals[i][1];
                priQ.offer(new int[]{r - l + 1, r});
                i++;
            }

            while (!priQ.isEmpty() && q > priQ.peek()[1])
            {
                priQ.poll();
            }
            res.put(q, priQ.isEmpty() ? -1 : priQ.peek()[0]);
        }

        int[] out = new int[queries.length];
        for (i = 0; i < queries.length; i++)
        {
            out[i] = res.get(queries[i]);
        }

        return out;
    }
}
