class Solution {
    public int reverseBits(int n) {
        int out = 0;
        int i = 0;

        while (n != 0)
        {
            out |= ((n & 1) << (31 - i));
            n >>>= 1;
            i++;
        }
        return out;
    }
}
