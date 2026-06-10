class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, curr):
            if i == n:
                if curr == target:
                    return 1
                return 0
            
            if (i, curr) in memo:
                return memo[(i, curr)]

            memo[(i, curr)] = dfs(i + 1, curr - nums[i]) + dfs(i + 1, curr + nums[i])

            return memo[(i, curr)]
            

        ret = dfs(0, 0)
        return ret if ret != -1 else 0