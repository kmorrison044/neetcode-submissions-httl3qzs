class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        tab = [n2 - j for j in range(n2 + 1)]
        newTab = [n2 - j for j in range(n2 + 1)]

        for i in range(n1 - 1, -1, -1):
            newTab[n2] = n1 - i
            for j in range(n2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    newTab[j] = tab[j + 1]
                else:
                    o1 = 1 + tab[j]
                    o2 = 1 + tab[j + 1]
                    o3 = 1 + newTab[j + 1]
                    newTab[j] = min(o1, o2, o3)

            tab = newTab.copy()

        return tab[0]