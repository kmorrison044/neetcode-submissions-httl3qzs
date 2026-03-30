class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Create a memo table that stores if s[i:j + 1] is a valid
        # substring
        memo = [[False] * n for _ in range(n)]
        # Initialize vars for return val
        idx, length = 0, 0

        # Use dp with bottom up approach. Iterate through the table
        # from the back of the list, then iterate j from the current
        # position of i to the end of the list. If both s[i] and s[j]
        # are the same character and if the characters within i and j
        # are palindromes, then i to j is a palindrome. There are
        # a couple edge cases to keep track of: if s[i] and s[j] are
        # equal, and the length of the substring is 3 or smaller, then
        # it is always going to be a palindrome.
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                    # If the above statement is true, then substring
                    # i to j is a palindrome, so memoize.
                    memo[i][j] = True
                    # Keep track of the longest substring
                    if length < (j - i + 1):
                        idx = i
                        length = j - i + 1
        
        # by keeping track of where the longest substring started, 
        # and the length of the substring, then we can grab the longest
        # substring from the parent string.
        return s[idx :  idx + length]