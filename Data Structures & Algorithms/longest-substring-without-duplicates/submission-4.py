class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp: dict[str, int] = {} # Initialize dictonary to store character: index
        l: int = 0 # Initialize left pointer
        res: int = 0 # Result for longest substr

        for r in range(len(s)): # Iterate right pointer
            if s[r] in mp: # Check if character already in map
                l = max(mp[s[r]] + 1, l) # Update left pointer to be the position
                # of duplicate or current position to ensure "l" does not
                # go backward.
            mp[s[r]] = r # Store char and position
            res = max(res, r-l+1) # Update res

        return res