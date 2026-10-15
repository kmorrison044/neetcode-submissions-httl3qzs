class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[None] * 2 for _ in range(n)]
        dp[n - 1][True] = max(0, nums[n - 1])
        dp[n - 1][False] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            for flag in [True, False]:
                if flag:
                    dp[i][flag] = max(0, nums[i] + dp[i + 1][True])
                else:
                    dp[i][flag] = max(dp[i + 1][False], nums[i] + dp[i + 1][True])
        
        return dp[0][False]