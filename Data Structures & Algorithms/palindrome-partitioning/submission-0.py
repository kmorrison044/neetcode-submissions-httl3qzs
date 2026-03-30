class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def backtack(i):
            # Check to see if i is in bounds. If not, append the part, because
            # below we've gaurenteed that it is a palindrome
            if i >= len(s):
                res.append(part.copy())
                return
            # Iterate through the list starting from where you currently are
            # till the end. Check if it is a palindrome. If so, append to part
            # list
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    backtack(j + 1)
                    part.pop()

        backtack(0)
        return res

    # Easy palindrome function
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True