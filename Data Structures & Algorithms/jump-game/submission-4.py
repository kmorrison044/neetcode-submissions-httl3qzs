class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            for opt in range(min(n, nums[i] + 1)):
                if i + opt >= n - 1 or dp[i + opt]:
                    dp[i] = True
                    break
        
        return dp[0]