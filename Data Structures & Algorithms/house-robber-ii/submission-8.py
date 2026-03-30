class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(skip):
            rob1, rob2 = 0, 0

            for i, num in enumerate(nums):
                if i == skip:
                    continue
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2

        # Create a helper function that does House robber 1, and call it twice,
        # once including n-1 but not 0, and once including 0, but not n-1. Compute
        # max between these values, and the first value of nums, if nums contains 1 element.
        return max(nums[0], helper(0), helper(n - 1))