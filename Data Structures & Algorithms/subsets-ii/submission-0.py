class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i: int, curr: List[int]):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            # Choice to include the current number:
            curr.append(nums[i])
            backtrack(i + 1, curr)
            
            # Choice to not include the current number:
            curr.pop()
            # Skip dups
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            
            backtrack(i + 1, curr)

        backtrack(0, [])
        return res