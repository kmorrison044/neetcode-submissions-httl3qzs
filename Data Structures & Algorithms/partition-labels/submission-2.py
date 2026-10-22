class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {ch : i for i, ch in enumerate(s)}

        res = []
        size = end = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, lastIdx[ch])

            if i == end:
                res.append(size)
                size = 0
        return res