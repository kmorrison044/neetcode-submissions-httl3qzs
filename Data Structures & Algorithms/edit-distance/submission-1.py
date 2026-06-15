class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        tab = [[float('inf')] * (n2 + 1) for _ in range(n1 + 1)]

        for j in range(n2 + 1):
            tab[n1][j] = n2 - j
        
        for i in range(n1 + 1):
            tab[i][n2] = n1 - i

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    tab[i][j] = tab[i + 1][j + 1]
                else:
                    o1 = 1 + tab[i + 1][j]
                    o2 = 1 + tab[i + 1][j + 1]
                    o3 = 1 + tab[i][j + 1]
                    tab[i][j] = min(o1, o2, o3)

        return tab[0][0]