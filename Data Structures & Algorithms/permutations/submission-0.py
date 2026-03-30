class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(pick: List[int], curr: List[int]):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    # Choose to pick this num and backtrack
                    pick[i] = True
                    curr.append(nums[i])
                    backtrack(pick, curr)

                    # Choose not to pick this num. Will be an option in
                    # the next backtrack call, so no need to recall 
                    # backtrack here.
                    pick[i] = False
                    curr.pop()
        
        backtrack([False]*len(nums), [])
        return res

