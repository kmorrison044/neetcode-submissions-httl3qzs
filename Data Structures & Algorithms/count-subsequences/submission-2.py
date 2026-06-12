class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        tab = [[0] * (nt + 1) for _ in range(ns + 1)]
        for i in range(ns + 1):
            tab[i][nt] = 1
        
        for i in range(ns - 1, -1, -1):
            for j in range(nt - 1, -1, -1):
                tab[i][j] = (tab[i + 1][j + 1] + tab[i + 1][j]
                             if s[i] == t[j] else tab[i + 1][j])
        
        return tab[0][0]