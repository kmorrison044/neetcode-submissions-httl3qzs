class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for i in range(len(intervals) - 1):
            it1 = intervals[i]
            it2 = intervals[i + 1]
            if it1[1] < it2[0]:
                res.append(it1)
                continue
            it2 = [min(it1[0], it2[0]), max(it1[1], it2[1])]
            intervals[i + 1] = it2
        
        res.append(intervals[-1])
        return res