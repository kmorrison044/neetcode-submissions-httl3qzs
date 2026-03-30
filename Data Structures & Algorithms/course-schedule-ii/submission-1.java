class Solution {
    private List<Integer> out = new ArrayList<>();
    private Set<Integer> cycle = new HashSet<>(), visit = new HashSet<>();
    private Map<Integer, List<Integer>> preMap = new HashMap<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        for (int cs = 0; cs < numCourses; cs++)
        {
            preMap.put(cs, new ArrayList<Integer>());
        }

        for (int[] pre : prerequisites)
        {
            preMap.get(pre[0]).add(pre[1]);
        }

        for (int cs = 0; cs < numCourses; cs++)
        {
            if (!dfs(cs))
            {
                return new int[0];
            }
        }

        return out.stream().mapToInt(Integer::intValue).toArray();
    }

    private boolean dfs(int cs)
    {
        if (visit.contains(cs))
        {
            return true;
        }
        if (cycle.contains(cs))
        {
            return false;
        }

        cycle.add(cs);
        for (int pre : preMap.get(cs))
        {
            if (!dfs(pre))
            {
                return false;
            }
        }
        cycle.remove(cs);

        visit.add(cs);
        out.add(cs);
        return true;
    }
}
