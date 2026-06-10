class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tot = sum(nums)

        if abs(target) > tot:
            return 0

        # Since we can have negative values for the current sum,
        # we need to offset it by 2 * total sum to account for all
        # the negative possibilities
        memo = [[-1] * (2 * tot + 1) for _ in range(n)]

        def dfs(i, curr):
            if i == n:
                return 1 if curr == target else 0
            
            # Remember in all these memo lookups there can be negative numbers.
            # That is why we did 2 * tot + 1 when initializing the memo table,
            # so that we can offset the negative values for curr by the total
            # sum to make it a positive index so we can appropriately access it
            # in the memo table.
            if memo[i][curr + tot] != -1:
                return memo[i][curr + tot]

            memo[i][curr + tot] = dfs(i + 1, curr - nums[i]) + dfs(i + 1, curr + nums[i])

            return memo[i][curr + tot]
            
        return dfs(0, 0)