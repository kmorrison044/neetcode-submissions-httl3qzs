class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tot = sum(nums)

        if abs(target) > tot:
            return 0

        # Since we can have negative values for the current sum,
        # we need to offset it by 2 * total sum to account for all
        # the negative possibilities
        tab = [[0] * (2 * tot + 1) for _ in range(n + 1)]
        # Base case: When i == n and we've reached the target (plus the offset),
        # then we've found and answer
        tab[n][target + tot] = 1

        for i in range(n - 1, -1, -1):
            # All possible values are from -tot (since all can be negative) to
            # tot (since all can be positive)
            for curr in range(-tot, tot + 1):
                # Create our two cases where we add nums[i] or subtract nums[i]
                add = curr + nums[i]
                sub = curr - nums[i]
                
                # Collect already calculated values, ensuring that your indices
                # are in bounds
                future_add = tab[i + 1][add + tot] if -tot <= add <= tot else 0
                future_sub = tab[i + 1][sub + tot] if -tot <= sub <= tot else 0

                # Calculate the current state and remember the offset due to negative
                # values
                tab[i][curr + tot] = future_add + future_sub

        # Return the beginning state. Remember the 0 index is actually -tot, so 
        # the real index where the value 0 lives is 0 + tot.
        return tab[0][0 + tot]