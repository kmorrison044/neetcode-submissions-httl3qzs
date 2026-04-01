class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        res = nums[0]

        for n in nums:
            tmp = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * tmp, n * currMin, n)

            res = max(res, currMax)
        
        return res