class Solution:
    def countBits(self, n: int) -> List[int]:
        # Intialize dp array from 0 to n
        dp = [0] * (n + 1)

        # loop from 0 to n
        for i in range(n + 1):
            # The number of bits at i is the number of bits we had for dp at i shifted by 1
            # plus the last bit of i (calculated by i & 1 to determine if i is 1 or 0).
            # This works since we should have the exact same number of bits as i >> 1 (which is
            # just knocking off the last bit of i) plus whatever the last bit of i is.
            dp[i] = dp[i >> 1] + (i & 1)
        
        # Return the dp array. Works in O(n) time.
        return dp