class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] memo = new boolean[n + 1];
        memo[n] = true;

        for (int i = n - 1; i >= 0; i--)
        {
            for (String w : wordDict)
            {
                if (i + w.length() <= n && s.startsWith(w, i))
                {
                    memo[i] = memo[i + w.length()];
                }
                if (memo[i])
                {
                    break;
                }
            }
        }

        return memo[0];
    }
}
