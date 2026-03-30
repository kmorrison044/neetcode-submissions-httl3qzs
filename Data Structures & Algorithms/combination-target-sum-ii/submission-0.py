class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(tot: int, i: int, curr: List[int]):
            if tot == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or tot >= target:
                return
            
            # Choice to select number:
            curr.append(candidates[i])
            backtrack(tot + candidates[i], i + 1, curr)

            # Choice to not select number:
            curr.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1

            backtrack(tot, i, curr)
        
        backtrack(0, 0, [])
        return res