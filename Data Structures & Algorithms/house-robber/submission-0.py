class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        

        memo = [-1] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, n):
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])
        
        return memo[-1]