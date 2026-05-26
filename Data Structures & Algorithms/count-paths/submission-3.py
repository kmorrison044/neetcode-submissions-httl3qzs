class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the tabulation table to be all 1s for the bottom row
        tab = [1] * n
        # Iterate starting from the second to last row and column, because the last row and
        # column are going to be all 1's.
        for _ in range (m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                # Add the current value of the element to the value immeditely to the right of it.
                # This accomodates both adding the bottom and the right, since we intialized the last row to 1s
                tab[j] += tab[j + 1]
        
        # Return the first value for total number of paths to reach the target.
        return tab[0]