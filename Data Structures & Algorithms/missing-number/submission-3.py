class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # We are iterating through nums which will be 0 to n - 1, so
        # intialize out to n
        out = n

        # Iterate through nums
        for i in range(n):
            # XOR the index and the number with our current total.
            # Every number that appears twice will cancel each other out
            # and what remains is the missing number.
            out ^= i ^ nums[i]
        
        # Return out
        return out