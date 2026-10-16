class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [float("inf") for _ in range(n)]

        def dfs(i):
            if memo[i] != float("inf"):
                return memo[i]
            if i == n - 1:
                return 0
            if nums[i] == 0:
                return float("inf")
            
            res = float("inf")
            end = min(n - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                memo[i] = min(memo[i], 1 + dfs(j))
            return memo[i]

        return dfs(0)