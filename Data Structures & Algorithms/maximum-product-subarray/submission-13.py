class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Memo table to store (current_max, current_min) for each index
        memo = {}

        def dp(i):
            # Base Case: The first element
            if i == 0:
                return nums[0], nums[0]
            
            # Return cached result if we've been here before
            if i in memo:
                return memo[i]
            
            # Recursive Step: Get max/min from the previous subproblem
            prev_max, prev_min = dp(i - 1)
            
            # Calculate current states
            curr_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            curr_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            
            # Store in memo table
            memo[i] = (curr_max, curr_min)
            return memo[i]

        # We need to find the max across all possible ending positions
        max_res = nums[0]
        for i in range(len(nums)):
            curr_max, _ = dp(i)
            max_res = max(max_res, curr_max)
            
        return max_res