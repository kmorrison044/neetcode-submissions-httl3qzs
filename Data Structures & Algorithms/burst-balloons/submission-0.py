class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Make ones on both sides of the array to prevent
        # OOB calculations
        nums = [1] + nums + [1]
        n = len(nums)
        # We are caching the max coins you can get
        # in a specific subarray.
        memo = [[-1] * n for _ in range(n)]

        def dfs(l, r):
            # Base case
            if l > r:
                return 0
            # Return cached value of max coins you can get
            # in a particular subarray.
            if memo[l][r] != -1:
                return memo[l][r]
            
            for i in range(l, r + 1):
                # Since we are popping nums[i] last, we know the value to the left and
                # right of the bounds of the subarray are the values that should also
                # be collected, since every other ballon in the subarray has already been
                # popped.
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # Analyze the subarrays to the left and right of the current pointer.
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                # Collect the max amount of coins
                memo[l][r] = max(memo[l][r], coins)
            return memo[l][r]
        
        # Since we added ones on each end of the array, start at 1 and the pointer
        # before the last element of the array.
        return dfs(1, n - 2)
