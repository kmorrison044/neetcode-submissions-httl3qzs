class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)

        tab = [[False for _ in range(np + 1)] for _ in range(ns + 1)]
        tab[ns][np] = True

        for i in range(ns, -1, -1):
            for j in range(np - 1, -1, -1):
                match = i < ns and (s[i] == p[j] or p[j] == '.')
                if j + 1 < np and p[j + 1] == '*':
                    tab[i][j] = tab[i][j + 2] or (match and tab[i + 1][j])
                elif match:
                    tab[i][j] = tab[i + 1][j + 1]

        return tab[0][0]