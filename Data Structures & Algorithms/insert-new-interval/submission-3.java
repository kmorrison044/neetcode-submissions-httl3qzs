class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0)
        {
            return new int[][]{newInterval};
        }

        int l = 0, r = intervals.length - 1;
        int targ = newInterval[0];

        while (l <= r)
        {
            int mid = l + (r - l) / 2;
            if (intervals[mid][0] > targ)
            {
                r = mid - 1;
            }
            else
            {
                l = mid + 1;
            }
        }

        List<int[]> res = new ArrayList<>();
        for (int i = 0; i < l; i++)
        {
            res.add(intervals[i]);
        }
        res.add(newInterval);
        for (int i = l; i < intervals.length; i++)
        {
            res.add(intervals[i]);
        }

        List<int[]> merged = new ArrayList<>();
        for (int[] it : res)
        {
            if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < it[0])
            {
                merged.add(it);
            }
            else
            {
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], it[1]);
            }
        }
        return merged.toArray(new int[0][]);
    }
}
