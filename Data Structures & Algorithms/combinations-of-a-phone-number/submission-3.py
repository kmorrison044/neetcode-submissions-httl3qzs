class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Map the digits to the chars
        charMap = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'], 
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'], 
                   '6': ['m', 'n', 'o'], 
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}

        res, curr = [], []

        def backtrack(i):
            # When we reach the len of digits, append and return
            if i >= len(digits):
                res.append("".join(curr.copy()))
                return
            
            # Iterate through the characters the current digit is mapped too,
            # Add it to your array, then call backtrack again after increasing your
            # iterator. This ensures that every combination is visited.
            for c in charMap[digits[i]]:
                curr.append(c)
                backtrack(i + 1)
                curr.pop()
        
        if digits:
            backtrack(0)
        return res

