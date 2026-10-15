class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[None] * 2 for _ in range(n)]
        
        def dfs(i: int, flag: bool):
            if i == n - 1:
                return max(0, nums[i]) if flag else nums[i]
            if memo[i][flag] is not None:
                return memo[i][flag]
            if flag:
                memo[i][flag] = max(0, nums[i] + dfs(i + 1, True))
            else:
                memo[i][flag] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            
            return memo[i][flag]
        
        return dfs(0, False)
