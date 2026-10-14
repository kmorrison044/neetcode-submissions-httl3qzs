class Solution {
    private Map<Character, Set<Character>> adj; 
    private Map<Character, Boolean> visited;
    private List<Character> ret;

    public String foreignDictionary(String[] words) {
        adj = new HashMap<>();
        for (String w : words)
        {
            for (char c : w.toCharArray())
            {
                adj.putIfAbsent(c, new HashSet());
            }
        }

        visited = new HashMap<>();
        ret = new ArrayList<>();
        int n = words.length;

        for (int i = 0; i < n - 1; i++)
        {
            String w1 = words[i], w2 = words[i + 1];
            int minLen = Math.min(w1.length(), w2.length());
            if (w1.length() > w2.length() && w1.substring(0, minLen).equals(w2.substring(0, minLen)))
            {
                return "";
            }

            for (int j = 0; j < minLen; j++)
            {
                if (w1.charAt(j) != w2.charAt(j))
                {
                    adj.get(w1.charAt(j)).add(w2.charAt(j));
                    break;
                }
            }
        }

        for (char c : adj.keySet())
        {
            if (!dfs(c))
            {
                return "";
            }
        }

        Collections.reverse(ret);
        StringBuilder sb = new StringBuilder();
        for (char c : ret)
        {
            sb.append(c);
        }
        return sb.toString();
    }

    private Boolean dfs(char node)
    {
        if (visited.containsKey(node))
        {
            return !visited.get(node);
        }

        visited.put(node, true);

        for (char nei : adj.get(node))
        {
            if (!dfs(nei))
            {
                return false;
            }
        }

        visited.put(node, false);
        ret.add(node);
        return true;
    }
}
