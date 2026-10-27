class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        res.add(intervals[0]);

        for (int[] it : intervals)
        {
            int start = it[0], end = it[1];
            int lastEnd = res.get(res.size() - 1)[1];

            if (start <= lastEnd)
            {
                res.get(res.size() - 1)[1] = Math.max(lastEnd, end);
            }
            else
            {
                res.add(it);
            }
        }

        return res.toArray(new int[0][]);
    }
}
