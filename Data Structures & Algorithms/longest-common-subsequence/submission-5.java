class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] tab = new int[text1.length() + 1][text2.length() + 1];

        for (int i = 0; i < tab.length; i++)
        {
            tab[i][text2.length()] = 0;
        }

        for (int i = 0; i < tab[text1.length()].length; i++)
        {
            tab[text1.length()][i] = 0;
        }

        for (int i = text1.length() - 1; i >= 0; i--)
        {
            for (int j = text2.length() - 1; j >= 0; j--)
            {
                if (text1.charAt(i) == text2.charAt(j))
                {
                    tab[i][j] = 1 + tab[i + 1][j + 1];
                }
                else
                {
                    tab[i][j] = Math.max(tab[i + 1][j], tab[i][j + 1]);
                }
            }
        }
        return tab[0][0];
    }
}