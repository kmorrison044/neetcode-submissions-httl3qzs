class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        out = sum(range(n + 1))
        
        for num in nums:
            out -= num
        
        return out