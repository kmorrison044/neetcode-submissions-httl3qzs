class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(tot: int, i: int, curr: List[int]):
            if tot == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or tot > target:
                return
            
            curr.append(nums[i])
            backtrack(tot + nums[i], i, curr)
            curr.pop()
            backtrack(tot, i+1, curr)
        
        backtrack(0, 0, [])
        return res
