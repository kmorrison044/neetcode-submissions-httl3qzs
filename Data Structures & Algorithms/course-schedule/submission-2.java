class Solution {
    private Set<Integer> visited = new HashSet<>();
    private Map<Integer, List<Integer>> preMap = new HashMap<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for (int i = 0; i < numCourses; i++)
        {
            preMap.put(i, new ArrayList<Integer>());
        }
        
        for (int[] pair : prerequisites)
        {
            preMap.get(pair[0]).add(pair[1]);
        }

        for (int cs = 0; cs < numCourses; cs++)
        {
            if (!dfs(cs))
            {
                return false;
            }
        }

        return true;
    }

    public boolean dfs(int cs)
    {
        if (visited.contains(cs))
        {
            return false;
        }

        visited.add(cs);
        for (int pre : preMap.get(cs))
        {
            if (!dfs(pre))
            {
                return false;
            }
        }
        visited.remove(cs);

        return true;
    }
}
