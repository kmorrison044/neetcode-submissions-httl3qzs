class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Create an array that stores the LIS at that particular index
        # to the end of the nums list. We know that each number by itself
        # would have the value 1.
        dp = [1] * n

        # Iterate down the list.
        for i in range(n - 1, -1, -1):
            # Iterate from current position to the end of the list
            for j in range(i + 1, len(nums)):
                # If nums[i] < nums[j], then set the LIS of the current position
                # to the max between its current value and 1 + the value of the memoization table.
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # Simply return the LIS by calculating the map of the dp array
        return max(dp)