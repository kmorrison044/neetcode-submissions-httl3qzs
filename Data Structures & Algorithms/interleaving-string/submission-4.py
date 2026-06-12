class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        # Initialize tab list. Need nx + 1 because the base case is when both pointers
        # reach the end of their list (think of the recursive case), then we know
        # that they can be successviely interleaved.
        tab = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        # Base case, when both pointers hit the end, then it is true.
        tab[n1][n2] = True
        
        # Iterate backwards
        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                # Skip base case so we don't overwrite it.
                if i == n1 and j == n2:
                    continue

                # Matches occur when one or both of the strings match a character
                # in s3. Check future blocks in the tab list to grab their value.
                match_s1 = tab[i + 1][j] if i < n1 and s1[i] == s3[i + j] else False
                match_s2 = tab[i][j + 1] if j < n2 and s2[j] == s3[i + j] else False

                tab[i][j] = match_s1 or match_s2
                
        return tab[0][0]