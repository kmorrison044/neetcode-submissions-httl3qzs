class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Combination, permutations, etc usually gonna be backtracking
        # Create the return var.
        res = []
        
        # Create backtrack function that keeps track of the 
        # current pointer to nums, the current total, and the 
        # list of potential numbers that sum to target
        def backtrack(tot: int, i: int, curr: List[int]):
            # Base case 1, we reached our target
            if tot == target:
                # Append a copy of curr, since lists get passed
                # by reference in python
                res.append(curr.copy())
                return

            # Base case 2, check pointer or if total is greater than
            # target
            if i >= len(nums) or tot > target:
                return
            
            # Choose to include the current number, update target,
            # keep pointer the same since you can reuse an unlimited
            # amount of times.
            curr.append(nums[i])
            backtrack(tot + nums[i], i, curr)

            # Choose not to include current number
            curr.pop()
            backtrack(tot, i+1, curr)
        
        backtrack(0, 0, [])
        return res
