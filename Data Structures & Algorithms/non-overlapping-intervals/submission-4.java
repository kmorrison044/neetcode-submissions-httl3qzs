class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt((int[] a) -> a[0])
                                            .thenComparingInt(a -> a[1]));
        
        int prevEnd = intervals[0][1];
        int out = 0;

        for (int i = 1; i < intervals.length; i++)
        {
            int start = intervals[i][0], end = intervals[i][1];
            if (start >= prevEnd)
            {
                prevEnd = end;
            }
            else
            {
                out++;
                prevEnd = Math.min(prevEnd, end);
            }
        }
        return out;
    }
}
