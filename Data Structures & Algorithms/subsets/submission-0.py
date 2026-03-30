class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []

        def backtrack(i):
            if i >= len(nums):
                res.append(stack.copy())
                return
            
            # decision to include nums[i]
            stack.append(nums[i])
            backtrack(i+1)

            # decision to NOT include nums[i]
            stack.pop()
            backtrack(i+1)

        backtrack(0)
        return res