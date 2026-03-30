class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Returning "all" possible things of a certain criteria hints at backtracking
        res = []
    
        def backtrack(stack: List[string], openN: int, closedN: int):
            if closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                # Choice to include open paranthesis:
                stack.append("(")
                backtrack(stack, openN + 1, closedN)
                # Choice not to include open paranthesis:
                stack.pop()

            if openN > closedN:
                # Choice to include closed paranthesis:
                stack.append(")")
                backtrack(stack, openN, closedN + 1)
                # Choice not to include closed paranthesis:
                stack.pop()

        backtrack([], 0, 0)
        return res
            


        