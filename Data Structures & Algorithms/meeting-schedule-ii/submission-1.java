/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        List<int[]> times = new ArrayList<>();
        for (Interval it : intervals)
        {
            times.add(new int[]{it.start, 1});
            times.add(new int[]{it.end, -1});
        }

        times.sort(Comparator.comparingInt((int[] x) -> x[0])
                            .thenComparingInt(x -> x[1]));

        int res = 0, count = 0;
        for (int[] t : times)
        {
            count += t[1];
            res = Math.max(res, count);
        }

        return res;
    }
}
