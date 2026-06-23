class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Intialize cnt and res vars
        cnt = 0
        res = 0
        # Iterate through each number
        for num in nums:
            # Increament count if num is 1 else, reset count to 0
            cnt = cnt + 1 if num else 0
            # Calulate max at each iteration
            res = max(res, cnt)
        
        return res
