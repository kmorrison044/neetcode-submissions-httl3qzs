class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n ^ 0 = n
        for num in nums:
            # By XORing all the numbers together, duplicate numbers will cancel out
            # And thus the remaining number will be contained in res.
            res ^= num;
        return res