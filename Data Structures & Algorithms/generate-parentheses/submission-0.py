class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ret = []

        def backtrack(openN, closedN):
            if openN and closedN == n:
                ret.append("".join(stack))
                return
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

        backtrack(0, 0)
        return ret