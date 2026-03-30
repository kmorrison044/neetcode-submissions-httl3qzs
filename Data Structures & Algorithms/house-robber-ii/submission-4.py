class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def helper(numbers):
            n = len(numbers)
            rob1, rob2 = 0, 0

            for n in numbers:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2

        return max(nums[0], helper(nums[:n-1]), helper(nums[1:]))
        
