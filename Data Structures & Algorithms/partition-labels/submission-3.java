class Solution {
    public List<Integer> partitionLabels(String s) {
        Map<Character, Integer> lastIdx = new HashMap<>();
        for (int i = 0; i < s.length(); i++)
        {
            lastIdx.put(s.charAt(i), i);
        }

        int size = 0, end = 0;
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < s.length(); i++)
        {
            size++;
            end = Math.max(end, lastIdx.get(s.charAt(i)));

            if (i == end)
            {
                res.add(size);
                size = 0;
            }
        }

        return res;
    }
}
