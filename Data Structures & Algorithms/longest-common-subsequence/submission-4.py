class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a tab table to store keys from previous visits. Out of bounds
        # are marked with a "0".
        tab = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # Iterate backwards through the texts
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If they are equal, add one plus the value of the next elements of both texts.
                if text1[i] == text2[j]:
                    tab[i][j] = 1 + tab[i + 1][j + 1]
                else:
                    # If not equal find the max between keeping the current text element the same and incrementing
                    # the other and vice-versa.
                    tab[i][j] = max(tab[i][j + 1], tab[i + 1][j])
        
        # Return the first index
        return tab[0][0]
