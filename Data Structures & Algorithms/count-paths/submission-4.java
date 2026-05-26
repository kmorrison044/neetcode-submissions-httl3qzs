class Solution {
    public int uniquePaths(int m, int n) {
        int[] tab = new int[n];
        Arrays.fill(tab, 1);

        for (int i = m - 2; i >= 0; i--)
        {
            for (int j = n - 2; j >= 0; j--)
            {
                tab[j] += tab[j + 1];
            }
        }

        return tab[0];
    }
}
