class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Spaced optmized dp. Since the solution only concerns
        # The current value and the previous value at any point,
        # we can just track the current value and previous value
        # and then return the final value at the end.

        # Initialize currMin and currMax to 1, since this a 
        # neutral number and doesn't effect the result of multiplication.
        currMin, currMax = 1, 1

        # Initialize res to the first value in nums
        # to have something to compare with.
        res = nums[0]

        for n in nums:
            # Since we are changing currMax in the next line,
            # we need to store it temporarily.
            tmp = currMax

            # Set currMax/currMin to the max/min between the current number
            # multiplied currMax and currMin, or just the current
            # number by itself, incase there is a 0. This will 
            # allow the multiplication chain to restart.
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * tmp, n * currMin, n)

            # Compare the currMax with the global max
            res = max(res, currMax)
        
        return res