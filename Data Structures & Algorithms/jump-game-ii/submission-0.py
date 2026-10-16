class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            end = min(n - 1, nums[i] + i)
            for j in range(i, end + 1):
                dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[0]