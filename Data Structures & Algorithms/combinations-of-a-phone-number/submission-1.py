class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charMap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res, curr = [], []

        def backtrack(i):
            if i >= len(digits):
                if curr:
                    res.append("".join(curr.copy()))
                return
            
            for c in charMap[digits[i]]:
                curr.append(c)
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return res

