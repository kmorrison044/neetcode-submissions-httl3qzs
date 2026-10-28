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
    public boolean canAttendMeetings(List<Interval> intervals) {
        if (intervals.size() == 0)
        {
            return true;
        }
        intervals.sort(Comparator.comparingInt((Interval a) -> a.start)
                                    .thenComparingInt((Interval a) -> a.end));
        int prevEnd = intervals.get(0).end;

        for (int i = 1; i < intervals.size(); i++)
        {
            if (intervals.get(i).start < prevEnd)
            {
                return false;
            }
            prevEnd = intervals.get(i).end;
        }

        return true;
    }
}
