class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # For one pass go ahead an initialize the res array with 2 * n
        # elements
        res = [0] * 2 * n

        for i, num in enumerate(nums):
            # Set both i and i + n in one pass and done
            res[i] = res[i + n] = num
        
        return res
