class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<String> q = new ArrayDeque<>();
        Set<String> words = new HashSet<>(wordList);
        int res = 0;

        if (beginWord.equals(endWord) || !words.contains(endWord))
        {
            return 0;
        }

        q.offer(beginWord);
        while (!q.isEmpty())
        {
            res++;
            int size = q.size();
            for (int i = 0; i < size; i++)
            {
                String word = q.poll();
                if (word.equals(endWord))
                {
                    return res;
                }

                for (char c = 'a'; c <= 'z'; c++)
                {
                    for (int j = 0; j < word.length(); j++)
                    {
                        if (word.charAt(j) == c)
                        {
                            continue;
                        }

                        String pot = word.substring(0, j) + c + word.substring(j + 1);
                        if (words.contains(pot))
                        {
                            q.offer(pot);
                            words.remove(pot);
                        }
                    }
                }
            }
        }
        return 0;
    }
}
