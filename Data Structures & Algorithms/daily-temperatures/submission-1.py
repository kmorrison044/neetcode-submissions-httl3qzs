class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        max_in_stack = float("-inf")
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                idx, temp = stack.pop()
                res[idx] = i - idx
            stack.append((i, t))
            print(stack)

        return res