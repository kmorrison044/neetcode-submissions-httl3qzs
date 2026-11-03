class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        out = n

        for i in range(n):
            out ^= i ^ nums[i]
        
        return out