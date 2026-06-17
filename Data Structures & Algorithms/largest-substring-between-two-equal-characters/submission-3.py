class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstSeen = {}
        n = len(s)

        res = -1
        for i, c in enumerate(s):
            if c in firstSeen:
                res = max(res, i - firstSeen[c] - 1)
            else:
                firstSeen[c] = i
        
        return res
