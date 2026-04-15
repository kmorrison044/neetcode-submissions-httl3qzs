class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Make a memo list for every position in s where memo[i]
        # Represents if you can split up that sublist into words
        # in wordDict.
        n = len(s)
        memo = [False] * (n + 1)
        
        # Make the last position true, because it is the base case
        memo[n] = True

        # Decrement from the end of the list to the beginning
        for i in range(n - 1, -1, -1):
            # Check every word in wordDict
            for w in wordDict:
                # If the current index plus the length of the current word is less than or equal
                # to the length of s, and if the substring equals the word we are checking, then we
                if (i + len(w) - 1) < n and s[i : i + len(w)] == w:
                    # If the above is true, we can set our memo list for the current position 
                    # to be the value of the current position plus the length of the word. 
                    # Remember that memo[n] is the base case.
                    memo[i] = memo[i + len(w)]
                # If we found a word to make the current index true, we don't have to check all words,
                # We can skip to the next index.
                if memo[i]:
                    break
        
        # Return result of the memo table representing the beginning of s
        return memo[0]