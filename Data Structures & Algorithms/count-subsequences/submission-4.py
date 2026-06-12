class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        # If you look at the non-optimized tabulized solution
        # notice that we are only updating our current state based
        # off the row right beneath the current row. Because of this,
        # we don't have to build the whole ns x nt matrix in memory. We
        # just keep two rows at a time to save memory
        tab = [0 for _ in range(nt + 1)]
        newTab = [0 for _ in range(nt + 1)]

        # Our base case is when we hit nt, this means we have found
        # a match.
        tab[nt] = newTab[nt] = 1
        
        # Iterate through all possible combos of i and j
        for i in range(ns - 1, -1, -1):
            for j in range(nt - 1, -1, -1):
                # Remember if we hit a match, we look at the next row (tab) and next
                # column (j + 1), that is, we look at the next gathered value for the
                # next char for both s and t. If we don't have a match, we just look
                # at the next gathered value for the next char in s.
                newTab[j] = (tab[j + 1] + tab[j]
                             if s[i] == t[j] else tab[j])

            # Make sure to COPY the values from newTab into tab, otherwise,
            # you just set tab to newTab in memory.
            tab = newTab.copy()
        
        return tab[0]