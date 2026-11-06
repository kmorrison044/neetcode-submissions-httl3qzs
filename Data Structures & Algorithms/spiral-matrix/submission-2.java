class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        int top = 0, bot = row - 1, l = 0, r = col - 1;
        List<Integer> res = new ArrayList<>();

        while (top <= bot && l <= r)
        {
            // Right
            for (int j = l; j <= r; j++)
            {
                res.add(matrix[top][j]);
            }
            top++;

            // Down
            for (int i = top; i <= bot; i++)
            {
                res.add(matrix[i][r]);
            }
            r--;

            // Left
            if (top <= bot)
            {
                for (int j = r; j >= l; j--)
                {
                    res.add(matrix[bot][j]);
                }
                bot--;
            }

            // Up
            if (l <= r)
            {
                for (int i = bot; i >= top; i--)
                {
                    res.add(matrix[i][l]);
                }
                l++;
            }
        }
        return res;
    }
}
