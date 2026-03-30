class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        max_in_stack = float("-inf")
        for i,t in enumerate(temperatures):
            s_len = len(stack)
            if s_len > 0:
                curr = s_len - 1
                while stack and t > stack[curr][1]:
                    res[stack[curr][0]] = i - stack[curr][0]
                    stack.pop()
                    curr -= 1
            stack.append((i, t))
            print(stack)

        return res